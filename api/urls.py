from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path("regular/", regularView.as_view(), name='regular'),
    path("regular/<siz>/listall/", regular_list_all, name='regular'),
    path("square/<siz>/listall/", square_list_all, name='regular'),
    path("square/",squareView.as_view(),name = "square"),
    path("size/",sizeView.as_view(),name="size"),
    path("topping/",toppingView.as_view(),name="topping"),
    path("update/<typeof>/<id>/<siz>",updateapizza,name="update"),
    path("delete/<id>/",deleteapizza,name="delete")
]