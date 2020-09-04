from django.contrib import admin
from django.urls import path
from main.views import index, detail, new, update, create, delete


urlpatterns = [
    path('',index, name="index"),
    path('detail/<int:student>',detail, name="detail"),
    path('new/',new, name="new"),
    path('update/<int:student>',update, name="update"),
    path('delete/<int:student>',delete, name="delete"),
    path('create/', create, name="create"),
]
