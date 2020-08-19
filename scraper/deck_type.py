from typing import Optional, List
from dataclasses import dataclass

DeckTupleType = (
    str,
    str,
    Optional[str],
    Optional[str],
    Optional[str],
    Optional[str],
    Optional[str],
)


@dataclass
class Deck:
    deckType: str
    commander: str
    commander_link: Optional[str]
    decklist: Optional[str]
    video: Optional[str]
    commander_img: Optional[str]
    scryfall: Optional[str]

    def as_tuple(self) -> DeckTupleType:
        return (
            self.deckType,
            self.commander,
            self.commander_link,
            self.decklist,
            self.video,
            self.commander_img,
            self.scryfall
        )
