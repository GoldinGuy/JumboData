import time
from typing import List, Dict
from datetime import datetime
import psycopg2
import psycopg2.extras
import psycopg2.extensions
import dateparser
import logging
import os
from .tappedOut import TappedOutScraper


class Scraper:
    db_conn: psycopg2.extensions.connection
    db_cur: psycopg2.extensions.cursor
    logger: logging.Logger

    # Delay between scrapes in minutes
    interval = 15

    def __init__(self, database_url: str):
        self.logger = logging.getLogger("scraper")

        self.db_conn = psycopg2.connect(database_url)
        self.db_cur = self.db_conn.cursor()

        self.logger.debug("Connected to db")

        interval = os.environ.get("SCRAPER_INTERVAL")
        if interval is not None:
            self.interval = int(interval)
        self.logger.info(
            "Scraping interval set to {} days".format(self.interval))

    def run(self):
        """
        Run the scraper - This will continuously update the database
        """
        while True:
            self.logger.info("Scraping...")
            decks = []
            try:
                decks.extend(TappedOutScraper.scrape_decks())
            except Exception as e:
                self.logger.exception(
                    'Scraper for TappedOut raised an exception'
                )

            self.insert_decks(decks)

            self.logger.info(
                "Done scraping, sleeping for {} days".format(self.interval)
            )
            time.sleep(self.interval * (60 * 60 * 24))

    def test_list(self):
        """
        Display a list showing scraped articles
        """

        decks = []
        try:
            decks.extend(TappedOutScraper.scrape_decks())
        except Exception as e:
            self.logger.exception(
                'Scraper for site TappedOut raised an exception'
            )

        print("Collected {} decks:".format(len(decks)))
        for deck in decks:
            print("#", deck.deckType)
            print("  commander    =", deck.commander)
            print("  image  =", deck.commander_img)
            print("  video  =", deck.video)
            if deck.decklist is not None:
                print("  decklist   =", deck.decklist)
            print()

        if os.environ.get("JUMBO_WRITE_TO_DB") is not None:
            self.insert_decks(decks)

    def insert_decks(self, decks):
        psycopg2.extras.execute_batch(
            self.db_cur,
            "insert into decks"
            "(deckType, commander, commander_link, decklist, video, commander_img, scryfall) values"
            "(%s, %s, %s, %s, %s, %s, %s) on conflict do nothing",
            [i.as_tuple() for i in decks],
        )
        self.db_conn.commit()
