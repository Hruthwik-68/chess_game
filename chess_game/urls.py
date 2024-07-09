from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('move_white/', views.move_white, name='move_white'),
    path('move_black/', views.move_black, name='move_black'),
        path('restart/', views.restart_game, name='restart_game'),

]
