from django.contrib import admin
from django.urls import path,include
from TrangChu import views

app_name = 'TrangChu'
urlpatterns = [
    path('', views.trangchu,name='trangchu'),
    path('student/', views.student,name='student'),
    path('teacher/', views.teacher,name='teacher'),
    path('login/', views.login,name='edit'),
    path('edit/', views.edit,name='login'),

]
