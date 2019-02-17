import xlrd
from pymongo import MongoClient

class UpdateDocuments:
    def __init__(self): 
        loc = ("../bank.xls")
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        client = MongoClient("mongodb://Sanyam:abcd123@cluster0-shard-00-00-tctra.mongodb.net:27017,cluster0-shard-00-01-tctra.mongodb.net:27017,cluster0-shard-00-02-tctra.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
        db=client.test
        coll=db.regs        
        unverified_docs = coll.find({'hostelv':'false'})
        for ob in unverified_docs:
            du = ob['hostel']
            i=0
            for i in range(0,sheet.nrows):
                if du in sheet.cell_value(i,3):
                    if(int(ob['rollno']) in (sheet.cell_value(i,2)).str()):
                        coll.update_one({'hostel':du},{ "$set" : {'hostelv':'true'}})
                        break