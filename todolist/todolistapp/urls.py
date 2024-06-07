from django.urls import path,include
from todolistapp import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('loginview/', views.loginview, name='loginview'),
    path('registerview/', views.registerview, name='registerview'),
    path('noteview/', views.noteview, name='noteview'),
    path('deletenote/<int:id>/',views.deletenote ,name="deletenote"),
    path('editnote/<int:id>/',views.editnote ,name="editnote"),
    path('updatenote/<int:id>/',views.updatenote ,name="updatenote"),
    path('addnote/',views.addnote ,name="addnote"),
]
