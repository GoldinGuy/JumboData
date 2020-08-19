from bs4 import BeautifulSoup
import requests
from typing import List
from .deck_type import Deck
import re

# links = ['/mtg-decks/avacyn-control-4/', '/mtg-decks/god-eternal-oketra-white-weenie/', '/mtg-decks/kumena-folk/', '/mtg-decks/inniaz-thieving-flyers/', '/mtg-decks/muldrotha-lands-are-everything/', '/mtg-decks/will-and-rowan-polywalkers/', '/mtg-decks/ruric-thar-on-a-budget-4/', '/mtg-decks/golos-epic-topdecks/', '/mtg-decks/sisay-sanctums-wonder-woman/', '/mtg-decks/saskia-is-legendary-1/', '/mtg-decks/28-07-20-braids-commander-adept-copy/', '/mtg-decks/my-akiri-tymna-artifact-aggro-copy/', '/mtg-decks/grimlock-transformers-2/', '/mtg-decks/kinnan-competitive-prodigy-cedh/', '/mtg-decks/counter-strike-mtgo-edition/', '/mtg-decks/24-10-19-counterstrike/', '/mtg-decks/akiri-tymna-artifact-aggro/', '/mtg-decks/29-07-20-mono-black-enchantments-copy/', '/mtg-decks/kenrith-all-the-politics/', '/mtg-decks/breya-commander-2016-budget-upgrade/', '/mtg-decks/atraxa-commander-16-budget-upgrade/', '/mtg-decks/gonti-and-the-monoblack-etb-deck-copy-2/', '/mtg-decks/22-08-17-budget-brago/', '/mtg-decks/akiri-tymna-artifact-aggro-budget-ish/', '/mtg-decks/gahiji-honored-one-budget-1/', '/mtg-decks/braids-commander-adept-budget/', '/mtg-decks/vorel-of-many-counters-1/', '/mtg-decks/hazezon-token-enchantress/', '/mtg-decks/winota-is-my-new-boros-favorite/', '/mtg-decks/06-11-16-kynaios-and-tiro/', '/mtg-decks/zedruu-the-pretty-good-hearted/', '/mtg-decks/super-budget-yorvo-smashes/', '/mtg-decks/tawnos-urzas-apprentice-commander-2018/', '/mtg-decks/thassa-blinks-the-best/', '/mtg-decks/tasigur-lands-that-isnt-three-grand/', '/mtg-decks/cards-dudes-xyris-the-writhing-storm/', '/mtg-decks/spike-tournament-winner/', '/mtg-decks/siona-captain-of-auras-3/', '/mtg-decks/exploring-sidisi-1/', '/mtg-decks/brallin-shabraz-shark-attack/', '/mtg-decks/selvala-live-build-experiment/', '/mtg-decks/saskia-is-calling-you-out/', '/mtg-decks/razaketh-demon-days-budget/', '/mtg-decks/03-01-18-ramos-spellslinger/', '/mtg-decks/29-12-18-rakdos-lord-of-demons/', '/mtg-decks/niv-miz-its-time/', '/mtg-decks/legendary-hijinks-1/', '/mtg-decks/leovold-the-strictly-worse-edric-of-test/', '/mtg-decks/leovold-try-hard-of-test/', '/mtg-decks/kinnan-ramp-into-monsters/', '/mtg-decks/karametra-creatures-1/', '/mtg-decks/jhoira-a-competitive-captain/', '/mtg-decks/isperia-flyers-on-a-budget/', '/mtg-decks/gyrus-waker-of-corpses-commander-2018/', '/mtg-decks/gonti-and-the-monoblack-etb-deck/', '/mtg-decks/grimlock-win-1/', '/mtg-decks/ezuri-budget-elves-2/', '/mtg-decks/17-01-18-UZa-elenda-aristocrats/', '/mtg-decks/bruvac-mill-in-commander/', '/mtg-decks/angels-mixed-with-angels-1/', '/mtg-decks/braids-commander-adept-3/', '/mtg-decks/20-09-17-brago-blink-king/', '/mtg-decks/how-do-we-build-alela/', '/mtg-decks/adriana-anthem-commander/', '/mtg-decks/adeliz-wizard-tempo/', '/mtg-decks/team-fog-1/', '/mtg-decks/zurzoth-chaotic-devils/', '/mtg-decks/kenrith-king-of-politics-3/', '/mtg-decks/radha-land-matters-1/', '/mtg-decks/super-comander-deck/', '/mtg-decks/everyone-is-aggro-now/', '/mtg-decks/aquaman-themed-thryx/', '/mtg-decks/21-05-20-zaxara-x-spells/', '/mtg-decks/obosh-is-oddly-powerful/', '/mtg-decks/brawlin-wintoa/', '/mtg-decks/aminatou-the-fateshifter-commander-2018/', '/mtg-decks/godzilla-the-powerful/', '/mtg-decks/kroxa-discard-reanimator-combo-everything/', '/mtg-decks/revel-in-artifacts/', '/mtg-decks/saheeli-gifted-artificer-commander-2018/', '/mtg-decks/jenara-bring-your-dice-budget/', '/mtg-decks/24-10-16-AYb-atraxa/', '/mtg-decks/inalla-wizard-swarm/', '/mtg-decks/cowboy-bebop-inspired-mathas-deck/', '/mtg-decks/27-01-20-rzZ-so-many-rats/', '/mtg-decks/jodah-big-mana-tribal-1/', '/mtg-decks/estrid-enchantments-commander-2018/', '/mtg-decks/lord-windgrace-lands-commander-2018/', '/mtg-decks/diaochan-all-your-things/', '/mtg-decks/heliod-is-the-best/', '/mtg-decks/merieke-tapnsteal/', '/mtg-decks/torbran-massive-damage/', '/mtg-decks/competitive-smasher-compilation/', '/mtg-decks/08-09-16-hanna/', '/mtg-decks/rashmi-eternally-cascading/', '/mtg-decks/20-08-16-GPF-grenzo-havoc-raiser/', '/mtg-decks/jhoira-the-izzet-artificer-we-asked-for/', '/mtg-decks/duel-leovold/', '/mtg-decks/wheeling-titans/', '/mtg-decks/26-10-16-jTp-breya/', '/mtg-decks/huatli-an-ass-aggro-oathbreaker/', '/mtg-decks/feather-the-new-boros-hotness/', '/mtg-decks/neheb-dreadhorde-champion-war-of-the-spark-spells/', '/mtg-decks/mirror-ally-enchantress/', '/mtg-decks/tiny-leovold-2/', '/mtg-decks/mtg-arena-singleton-sultai-midrange-wins-games/', '/mtg-decks/persistent-advisor-tribal-mill-chantment/', '/mtg-decks/30-01-19-zBd-jlks-judith-game-knights-23-copy/', '/mtg-decks/nikya-of-the-old-ways-creatures/', '/mtg-decks/prime-speaking-vannifar/', '/mtg-decks/singleton-bw-legend-tribal/', '/mtg-decks/singleton-azorius-artifacts/', '/mtg-decks/samut-oh-the-humanity-1/', '/mtg-decks/20-08-16-DRS-selvala/', '/mtg-decks/omnath-is-disgruntled/', '/mtg-decks/16-08-18-xantcha-sleeper-agent/', '/mtg-decks/scarab-god-zombie-etbs-1/', '/mtg-decks/lyra-angel-bringer-1/', '/mtg-decks/neheb-damage-ramp-1/', '/mtg-decks/muldrotha-the-unyielding-graveyard-1/', '/mtg-decks/hazezon-tamar-and-his-sand-warriors/', '/mtg-decks/the-meren-midrange-machine/', '/mtg-decks/locusts-everywhere-2/', '/mtg-decks/tishana-maro-tribal-1/', '/mtg-decks/pir-toothy-battle-buds/', '/mtg-decks/tetsuko-sneaky-sneaky-umezawa/', '/mtg-decks/aryel-knight-of-knights-2/', '/mtg-decks/unusual-atraxa-a-gp-vegas-showdown-build/', '/mtg-decks/firesong-and-sunspeaker-boros-bros/', '/mtg-decks/yargle-will-eat-you-and-your-commander-deck/', '/mtg-decks/slimefoot-aristocratic-saprolings-1/', '/mtg-decks/special-specter-spectacle-1/', '/mtg-decks/angus-moneybags-a-19000-commander-deck/', '/mtg-decks/kazuul-tyrant-of-commander-tables/', '/mtg-decks/brawling-hazoret/', '/mtg-decks/brawling-scarab-god/', '/mtg-decks/brawling-huatli/', '/mtg-decks/brawling-grixis-control/', '/mtg-decks/brawling-azor/', '/mtg-decks/brion-armed-and-dangerous/', '/mtg-decks/ruric-thar-15-super-budget-commander-deck/', '/mtg-decks/azor-revolutionary-sphinx/', '/mtg-decks/22-12-17-merfolk-on-a-budget/', '/mtg-decks/krenko-budget-goblins/', '/mtg-decks/riku-of-many-combos-4/', '/mtg-decks/sultai-lands-matter-featuring-tasigur/', '/mtg-decks/razaketh-artifact-combos/', '/mtg-decks/the-scorpion-gods-venom/', '/mtg-decks/ezuri-tuned-infinite-elves/', '/mtg-decks/zadaaaaaahhhhhhh/', '/mtg-decks/temmet-token-ifacts/', '/mtg-decks/hapatra-poisons-everyone/', '/mtg-decks/hazoret-amonkhet-burn/', '/mtg-decks/ikrakondo-abzan-partners/', '/mtg-decks/22-03-17-land-ho/', '/mtg-decks/queen-marchesa-rules/', '/mtg-decks/kynaios-and-tiro-of-your-face/', '/mtg-decks/sneaky-stealing-sisters/', '/mtg-decks/saskia-commander-2016-budget-upgrades-1/', '/mtg-decks/enchantastic-god-tribal-1/', '/mtg-decks/05-11-16-Gfl-yidris/', '/mtg-decks/17-10-16-SAg-karlov/', '/mtg-decks/07-06-16-mono-black-control/', '/mtg-decks/karrthus-dragon-of-dragons/']

def scrape_decks() -> List[Deck]:
    try:
        url = 'http://tappedout.net/users/JumboCommander/mtg-decks/'
        response = requests.get(url, timeout=15)
        content = BeautifulSoup(response.content, "html.parser")
    except Exception as e:
        print(str(e))

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
        try:
            url = 'http://tappedout.net/users/JumboCommander/mtg-decks/' + '?&p=' + str(x) + '&page=' + str(x)
            response = requests.get(url, timeout=15)
            content = BeautifulSoup(response.content, "html.parser")
        except Exception as e:
            print(str(e))

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
        try:
            url = 'http://tappedout.net' + link
            response = requests.get(url, timeout=15)
            content = BeautifulSoup(response.content, "html.parser")
        except Exception as e:
            print(str(e))

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
