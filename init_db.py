import os
import psycopg2

DATABASE_URL = os.environ["DATABASE_URL"]

conn = psycopg2.connect(DATABASE_URL)  # , sslmode='require')
cur = conn.cursor()

print("Creating decks table...")
cur.execute(
    """
create table if not exists decks (
    deckType  text not null,
    commander  text not null,
    commander_link  text
        constraint decks_pk
            primary key,
    image_url   text,
    commander_link   text not null,
    decklist    text not null,
    video text, 
    commander_img  text,
    scryfall text
);"""
)

conn.commit()
cur.close()
conn.close()
