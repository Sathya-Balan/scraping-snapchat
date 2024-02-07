import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


# class mOngoDb:
#     def __init__(self) -> None:
#         pass

def insert_doc(mydict):
    try:
        print(mydict)
        existing_document = mycol.find_one(mydict)
        if not existing_document:
            document = mycol.insert_one(mydict)
            print("inserted successfully")
            return document.inserted_id
        else:
            return "document exist"
    
    except Exception as ex:
        raise ex
