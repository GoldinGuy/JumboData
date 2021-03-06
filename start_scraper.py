import os
import logging
import scraper


if __name__ == "__main__":
    DATABASE_URL = os.environ["DATABASE_URL"]

    if os.environ.get("JUMBO_DEBUG_LOGGING") is not None:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.ERROR)

    print('starting scraper...')
    scraper.Scraper(DATABASE_URL).run()
