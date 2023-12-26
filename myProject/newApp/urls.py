from django.urls import path
from . import views

urlpatterns = {
    1 : path('welcome/', views.welcome),
    2 : path('home/', views.home),
    3 : path('date/', views.date)
}