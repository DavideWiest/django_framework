
from datetime import datetime
from bson import ObjectId

def nonetypes_exist(d):
    exist = False
    errmsg = ""
    for k in d:
        if type(d[k]) == type(None):
            exist = True
            errmsg = f"Key {k} cannot be type NoneType"
    return exist, errmsg


class BaseStruct():
    def __init__(self, variable):
        self.variable = variable

        self._id = ObjectId()
        self.created_at = datetime.now().strftime("%m-%d-%Y, %H:%M:%S")

class BaseCol():
    def __init__(self, mm, col):
        self.mm = mm
        self.col = col
    
    def struct_from_dict(self, d):
        exist, errmsg = nonetypes_exist(d)
        if exist:
            raise TypeError(errmsg)
        return BaseStruct(d["variable"])
    
    def create(self, obj: BaseStruct):
        obj_dict = obj.__dict__
        self.col.insert_one(obj_dict)
        return str(obj._id)

    def read(self, query, return_fields={}):
        docs = self.col.find_one(query, return_fields)
        return docs
        
    def multiread(self, query, return_fields={}):
        docs = list(self.col.find_many(query, return_fields))
        return docs
    
    def update(self, query, update_fields, outside_set=False):
        update_dict = {"$set": update_fields} if not outside_set else update_fields
        self.col.update_one(query, update_dict)

    def multiupdate(self, query, update_fields, outside_set=False):
        update_dict = {"$set": update_fields} if not outside_set else update_fields
        self.col.update_many(query, update_dict)

    def delete(self, query):
        self.col.delete_one(query)

    def multidelete(self, query):
        self.col.delete_many(query)
    
    def get_all_field_ids(self, filter={}):
        docs = self.col.find(filter, {"_id": 1})
        return docs
    
    def exists(self, query):
        if isinstance(query, ObjectId):
            query = {"_id": query}
        docs = self.col.find_one(query)
        return bool(docs)

