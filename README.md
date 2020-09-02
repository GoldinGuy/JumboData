# Jumbo Database

[![Netlify Status](https://api.netlify.com/api/v1/badges/e06aba21-4039-43e3-9e3b-fb18c7d1e1c3/deploy-status)](https://app.netlify.com/sites/mystifying-goldberg-61d144/deploys)

An API that scrapes data for YouTube content and returns it in json form. Designed to be used as a resource for websites struggling with API quotas. Collect URL links, names, images, and other relevant information from videos, and decks.

## How to use it

JumboData can be accessed at `https://jumbo-data.herokuapp.com/latest_videos` for the latest video data

and `https://jumbo-data.herokuapp.com/deck_techs` for hundreds of deck techs

Content is returned in json form. Sample data is below:

        {"kind": "youtube", "nextPageToken": "CB4QAA", "items": [{"kind": "youtube#playlistItem", "etag": "\"qFhV4-MfWAvOxa-mFa9xiq_e-_c/1sAhJudj25EmjXLyFn0Xg8QoDO8\"", "id": "VVVQcVQyVUxhdDRXSXpXS3FwQUFPbElRLjU2QjQ0RjZEMTA1NTdDQzY=", "snippet": {"publishedAt": "2020-08-13T15:43:00.000Z", "channelId": "UCPqT2ULat4WIzWKqpAAOlIQ", "title": "Inniaz the Gale Force Thieving Flyers", "description": "Inniaz the Gale Force commander deck tech is a JUMP/START legendary that has a powerful flying pump and sinister table politics.\n\nDecklist: https://tappedout.net/mtg-decks/inniaz-thieving-flyers/\nI have a website! https://jumbocommander.com/\nCoolStuffInc has cool things! https://bit.ly/30U2kiU\nPatreon: https://www.patreon.com/JumboCommander\nTwitter:
        
        [{"deckType": "deckTechs", "commander": "Avacyn, Angel of Hope", "commander_link": "http://tappedout.net/mtg-card/avacyn-angel-of-hope/", "decklist": "http://tappedout.net/mtg-decks/avacyn-control-4/", "video": "https://www.youtube.com/watch?v=6HCB1TDzZW0", "commander_img": "https://img.scryfall.com/cards/art_crop/front/a/0/a0519776-3d86-4f7d-9c3b-71c1dfbf7e12.jpg?1596137881", "scryfall": "https://api.scryfall.com/cards/a0519776-3d86-4f7d-9c3b-71c1dfbf7e12"}, {"deckType": "deckTechs", "commander": "Kumena, Tyrant of Orazca", "commander_link": "http://tappedout.net/mtg-card/kumena-tyrant-of-orazca/", "decklist": "http://tappedout.net/mtg-decks/kumena-folk/", "video": "https://www.youtube.com/watch?v=LvcEow3-Tds", "commander_img": "https://img.scryfall.com/cards/art_crop/front/a/3/a3aef818-c896-46e6-aaff-56aee52a066c.jpg?1555040871", "scryfall": "https://api.scryfall.com/cards/a3aef818-c896-46e6-aaff-56aee52a066c"}, {"deckType": "deckTechs", "commander": "Inniaz, the Gale Force", "commander_link": "http://tappedout.net/mtg-card/inniaz-the-gale-force/", "decklist": "http://tappedout.net/mtg-decks/inniaz-thieving-flyers/", "video": "https://www.youtube.com/watch?v=iOj5VsfRHvY", "commander_img": "https://img.scryfall.com/cards/art_crop/front/b/2/b238485f-ef67-4295-892b-a10235368f74.jpg?1592705346", "scryfall": "https://api.scryfall.com/cards/b238485f-ef67-4295-892b-a10235368f74"}, {"deckType": "deckTechs", "commander": "Sisay, Weatherlight Captain", "commander_link": "http://tappedout.net/mtg-card/sisay-weatherlight-captain/", "decklist": "http://tappedout.net/mtg-decks/sisay-sanctums-wonder-woman/", "video": "https://www.youtube.com/watch?v=yKpZ7UJSIuI", "commander_img": "https://img.scryfall.com/cards/art_crop/front/5/a/5a293c45-1e73-4527-be2f-2dcd5c47b610.jpg?1582021363", "scryfall": "https://api.scryfall.com/cards/5a293c45-1e73-4527-be2f-2dcd5c47b610"},

Install dependencies with:

    pip3 install -r requirements.txt -U

[Latest Videos Json (last 24 hours)](https://jumbo-data.herokuapp.com/articles)

[Gameplay Json](https://jumbo-data.herokuapp.com/videos)

[Deck Techs Json](https://jumbo-data.herokuapp.com/deck_techs)

[Personal Decks Json](https://jumbo-data.herokuapp.com/my_decks)

[Site Using Jumbo API ](https://jumbocommander.com/)
