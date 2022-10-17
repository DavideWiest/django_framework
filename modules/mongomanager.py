import pymongo
import json
from bson.json_util import dumps

class MongoManager:
    def __init__(self, con_str, db_name, backup_con_str=None, backup_db_name=None):
        self.con_str = con_str
        self.backup_con_str = backup_con_str
        self.db_name = db_name
        self.backup_db_name = backup_db_name
        self.has_backup = bool(self.backup_con_str)
        
        self.connect()

        self.usercol = self.db["users"]
        self.stockcol = self.db["stocks"]
        self.stocklistcol = self.db["stocklists"]
        
    def connect(self):
        self.client = pymongo.MongoClient(self.con_str)
        self.db = self.client[self.db_name]

        if not self.has_backup:
            self.backup_client = None
            self.backup_db = None
        else:
            self.backup_client = pymongo.MongoClient(self.backup_con_str)
            self.backup_db = self.backup_client[self.backup_db_name]

    def export_to_json(self, filename):
        cursor = self.pcol.find({})
        with open(f"{filename}.json", "w") as file:
            json.dump(json.loads(dumps(cursor)), file)
