from pymongo import *
client = MongoClient("mongodb+srv://rishijha1709:rishijha1709@cluster0.2lkrw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test



class object():
    def getcoll(self,coll):
        return db[coll]
    def getaobject(self,data,coll):
        return coll.find_one(data)
    def insertaobject(self,data,coll):
        ins = coll.insert_one(data)
        return ins.inserted_id
    def getallobject(self,coll):
        res = []
        for doc in coll.find():
            res.append(doc)
        return res

    def updateaobject(self,coll,pdata,ndata):
        id = coll.update_one(pdata,{"$set":ndata})
        # return id.updated_count
        return "ok"
    def deleteaobject(self,id,coll):
        coll.delete_one({"_id":id})
    def todict(self):
        return self.__dict__

class size(object):
    coll = db["size"]
    def __init__(self,t):
        self.name = t
    
    def sizeispresent(self):
        sizes = self.getallobject(self.coll)
        res = False
        for i in sizes:
            if i["name"] == self.name:
                res =True
                break
            continue
        return res


class topping(object):
    coll = db["topping"]
    def __init__(self,tee):
        self.name = tee
    


class pizza(object):
    coll = db["pizza"]
    def __init__(self,t,ar:list,s:size):
        self.typeofpizza = t
        self.toppings= ar
        self.sizeofpizza= s.todict()
    def listallpizza(self):
        p = []
        pi ={}
        pizzas = self.getallobject(self.coll)
        for i in pizzas:
            if i["typeofpizza"]==self.typeofpizza and i["sizeofpizza"]==self.sizeofpizza:
                for j in i :
                    if j =="_id":
                        pi["id"] =str(i[j])
                    else:
                        pi[j] = i[j]
                p.append(pi)
                pi= {}
        return p
