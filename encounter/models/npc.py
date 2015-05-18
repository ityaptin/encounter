__author__ = 'it'

import re

from encounter.models import base

"""Contains a models for NPCs and monsters."""

ABILITY_TEMPLATE = re.compile(r"([a-zA-Z]{3}) (\d+)")
SAVE_TEMPLATE = re.compile(r"([a-zA-Z]{3,4}) ([+-]\d+)")

def read_ability_scores(abilities_raw="Str 0, Dex 0, Con 0, "
                                      "Int 0, Wis 0, Cha 0"):
    abilities = ABILITY_TEMPLATE.findall(abilities_raw)
    return dict((ability[0], int(ability[1])) for ability in abilities)

def read_saves(saves_raw='Fort +4, Ref +5, Will +2'):
    saves = SAVE_TEMPLATE.findall(saves_raw)
    return dict((save[0], int(save[1])) for save in saves)


class NPC(base.BaseModel):
    __name__ = "NPC"

    def __repr__(self):
        return ("{clazz}:"
                "name={name}, CR={cr}").format(
            clazz=self.__class__.__name__,
            name=getattr(self, "name", "npc"),
            cr=getattr(self, "cr", 0)
        )
