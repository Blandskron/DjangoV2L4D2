from django.urls import path
from . import views

urlpatterns = [
    path('', views.trivia_game, name='trivia_game'),
    path('check_answer/', views.check_answer, name='check_answer'),
]
