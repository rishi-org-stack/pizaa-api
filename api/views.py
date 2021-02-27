from bson.objectid import ObjectId
from django import http
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import json
from django.views import View
from pymongo import *
from api.models import object, pizza, size, topping
import api.response as res
class pizzaView(View):
    typeofpizza = "PIZZA"
    # size =''
    # toppings = []
    def get(self,request):
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # body["type"]=self.typeofpizza
        # s = pizza(self.typeofpizza,)
        
        # coll = s.getcoll("topping")
        # s.insertaobject(s.todict(),coll)
        # return HttpResponse(json.dumps({"ok":1}))
        return render(request,'pizza.html',{"typeofpizza":self.typeofpizza})

    def post(self,request):
        toppings = request.POST.get("topping").split(',')
        siz = request.POST.get("size")
        if len(toppings)>0:
            if len(siz)>0:
                s = size(siz)
                if s.sizeispresent():
                    p = pizza(self.typeofpizza,toppings,s)
                    id = p.insertaobject(p.todict(),p.coll)
                    res.success[201]["id"] = str(id)
                    return HttpResponse(json.dumps(res.success[201]))
                else:
                    return HttpResponse(json.dumps(res.errors[402]))
            else:
                return HttpResponse(json.dumps(res.errors[403]))
        else:
            return HttpResponse(json.dumps(res.errors[400]))
class regularView(pizzaView):
    typeofpizza = "regular"

class squareView(pizzaView):
    typeofpizza = "square"
    

class toppingView(View):
    pass

class sizeView(View):
    def get(self,request):
        return render(request,"size.html")
    def post(self,request):
        szn =request.POST.get("size")
        if len(szn)>0:
            s= size(szn)
            id = s.insertaobject(s.todict(),s.coll)
            res.success[200]["id"] = str(id)
            return HttpResponse(json.dumps(res.success[200]))
        else:
            return HttpResponse(json.dumps(res.errors[403]))

def regular_list_all(request,siz):
    p = pizza("regular",[],size(str(siz)))
    pizaas = p.listallpizza()
    return HttpResponse(json.dumps({"pizaas":pizaas}))

def square_list_all(request,siz):
    p = pizza("square",[],size(str(siz)))
    pizaas = p.listallpizza()
    return HttpResponse(json.dumps({"pizaas":pizaas}))

def updateapizza(request,typeof,id,siz):
    id = ObjectId(id)
    s= size(str(siz))
    if s.sizeispresent():
        p = pizza(str(typeof),id,s)
        p.updateaobject(p.coll,{"_id":id},{"sizeofpizaa":s.todict()})
        return HttpResponse(json.dumps(res.success[202]))
    else:
        return HttpResponse(json.dumps(res.errors[402]))
        


def deleteapizza(request,id):
    id = ObjectId(id)
    p = pizza('',id,size(''))
    p.deleteaobject(id,p.coll)
    return HttpResponse(json.dumps(res.success[203]))

# Create your views here.
def home(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    contents = body['content']
    return HttpResponse(contents)
