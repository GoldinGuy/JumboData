from bs4 import BeautifulSoup
import requests
from typing import List
from .deck_type import Deck
import re


def scrape_decks() -> List[Deck]:
    url = 'http://tappedout.net/users/JumboCommander/mtg-decks/'
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")

    print('determine number of pages')
    num_pages = 0
    for num in content.findAll('a', attrs={"class": "page-btn"}):
        if num.text.isdigit():
            if int(num.text) > num_pages:
                num_pages = int(num.text)

    print('get links to every deck')

    links = []
    y = 0
    for a in content.find_all('a', href=True):
        y += 1
        if '/mtg-decks/' in (a['href']) and '/accounts/' not in (a['href']) and '/search/' not in (
                a['href']) and y % 2 == 0:
            links.append(a['href'])

    x = 1
    while x < num_pages:
        x += 1
        url = 'http://tappedout.net/users/JumboCommander/mtg-decks/' + '?&p=' + str(x) + '&page=' + str(x)
        response = requests.get(url, timeout=5)
        content = BeautifulSoup(response.content, "html.parser")

        z = 0
        for a in content.find_all('a', href=True):
            z += 1
            if '/mtg-decks/' in (a['href']) and '/accounts/' not in (a['href']) and '/search/' not in (
                    a['href']) and z % 2 == 0:
                links.append(a['href'])

    print('get data from every deck')

    print(links)
    decks = []

    for link in links:
        url = 'http://tappedout.net' + link
        response = requests.get(url, timeout=5)
        content = BeautifulSoup(response.content, "html.parser")

        try:
            commander_link = ''
            for ul in content.findAll('ul', {'class': 'boardlist'}):
                for a in ul.findAll('a'):
                    for img in a.findAll('img', {'class': 'commander-img'}):
                        commander_link = str(a.get('href'))

            commander_url = 'http://tappedout.net' + commander_link
            commander_data = requests.get(commander_url, timeout=5)
            commander_content = BeautifulSoup(commander_data.content, "html.parser")
            temp = commander_content.find('h1').text
            commander = temp.replace('\n', '').strip()
        except(ConnectionError, Exception) as e:
            print("Exception is: ", e)
            commander_link = 'Unknown'
            commander = 'Unknown'

        try:
            temp = content.find('iframe').get('src').partition('href='),
            joined = ''.join(str(v) for v in temp)
            joined_rep = joined.replace('https://www.youtube.com/embed/', 'https://www.youtube.com/watch?v=')
            m = re.search("\('(.+?)',", str(joined_rep))
            video = m.group(1)
            print(video)
        except(ConnectionError, Exception) as e:
            print("Exception is: ", e)
            video = 'Unknown'

        try:
            jsonofabitch = requests.get('https://api.scryfall.com/cards/named?fuzzy=' + commander).json()
            commander_img = jsonofabitch.get('image_uris').get('art_crop')
            scryfall = jsonofabitch.get('uri')
        except(ConnectionError, Exception) as e:
            print("Exception is: ", e)
            commander_img = 'Unknown'
            scryfall = 'Unknown'

        try:
            if content.findAll(text='Commander / EDH') or (
                    'Commander / EDH' in content.find('a', {'class': 'btn btn-success btn-xs'}).text):
                deck_type = 'deckTechs'
            elif content.findAll(text='Commander / EDH*') or (
                    'Commander / EDH*' in content.find('a', {'class': 'btn btn-success btn-xs'}).text):
                deck_type = 'deckTechs'
            elif content.findAll(text='Casual') or (
                    'Casual' in content.find('a', {'class': 'btn btn-success btn-xs'}).text):
                deck_type = 'myDecks'
            else:
                deck_type = 'misc'

            deck_obj = Deck(
                deck_type,
                commander,
                'http://tappedout.net' + commander_link,
                'http://tappedout.net' + link,
                video,
                commander_img,
                scryfall,
            )
            decks.append(deck_obj)
        except Exception as e:
            print(e)

    print(decks)
    return decks
