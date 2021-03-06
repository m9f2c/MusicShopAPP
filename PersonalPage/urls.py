from django.urls import path

from PersonalPage import views

urlpatterns = [
    path('', views.home, name="personal_home_page"),
    path('sell_recording', views.sell_recording, name="sell_recording"),
    path('edit_recording', views.edit_recording, name="edit_recording"),
    path('correct_add', views.correct_add, name="correct_add"),
    path('edit_my_recording/<int:pk>', views.edit_my_recording, name="edit_my_recording"),
    path('delete_my_recording/<int:pk>', views.delete_my_recording, name="delete_my_recording"),
]
