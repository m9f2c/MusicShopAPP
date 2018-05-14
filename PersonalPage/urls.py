from django.urls import path

from PersonalPage import views

urlpatterns = [
    path('', views.home, name="personal_home_page"),
    path('sell_recording', views.sell_recording, name="sell_recording"),
    path('edit_recording', views.edit_recording, name="edit_recording"),

]
