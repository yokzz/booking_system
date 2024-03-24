from django.shortcuts import render
from booking.models import *

def get_rooms_list(request):
    rooms = Room.objects.all()
    context = {
               'rooms': rooms,
    }
    return render(request, 'booking/rooms_list.html', context)

def get_room_details(request, pk):
    room = Room.objects.get(id=pk)
    context = {
               'room': room,
    }
    return render(request, 'booking/room_details.html', context)