from django.urls import path, include
from .views import *

urlpatterns = [
    path('', get_rooms_list, name='rooms'),
    path('<int:pk>/', get_room_details, name='room'),
]
