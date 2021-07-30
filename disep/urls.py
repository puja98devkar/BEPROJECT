from django.contrib import admin
from django.urls import path
from  disep import views

urlpatterns = [
    path("",views.index,name='disep'),
    path("about",views.about,name='about'),
    path("services",views.services,name='script'),
    path("contact",views.contact,name='contact'),

]