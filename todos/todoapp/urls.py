
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.TodoList.as_view(), name='index'),
    path('new/', views.TodoCreate.as_view(), name='new'),
    path('<int:pk>/', views.TodoDetail.as_view(), name='todo'),
    path('<int:pk>/update', views.TodoUpdate.as_view(), name='update'),
    path('<int:pk>/delete', views.TodoDelete.as_view(), name='delete'),
]
