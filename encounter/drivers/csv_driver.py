__author__ = 'it'

import csv

from encounter.models import npc

class CSVReader(object):
    """Main csv stores at http://www.pathfindercommunity.net/home/databases/ ."""

    def __init__(self, filepath=None, db_name="monsters"):
        self.filepath = filepath
        self.db_name = db_name

    def read_all(self):
        models = []
        with open(self.filepath, "rb") as fb:
            reader = csv.reader(fb)
            fields = [field.lower() for field in reader.next()]
            for row_tuple in reader:
                body = dict(zip(fields, row_tuple))
                model = npc.NPC(self.db_name,
                                **body.copy())
                models.append(model)
        return models

