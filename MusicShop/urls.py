from django.urls import path

from MusicShop import views

urlpatterns = [
    path('', views.home, name="home_page"),

]
