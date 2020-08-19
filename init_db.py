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
    commander_link  text,
    image_url   text,
    decklist    text not null,
        constraint decks_pk
                primary key,
    video text, 
    commander_img  text,
    scryfall text
);"""
)

conn.commit()
cur.close()
conn.close()
