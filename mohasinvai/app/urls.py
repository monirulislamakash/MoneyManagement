from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="home"),
    path("add/",views.add,name="add"),
    path("debit/",views.debit,name="debit"),
    path("credit/",views.credit,name="credit"),
    path("monthly/",views.monthly,name="monthly"),
    path("search/",views.search,name="search"),
]
