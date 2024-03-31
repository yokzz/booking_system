from django.shortcuts import render, redirect
from booking.models import *
from django.http import HttpResponse

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

def booking_details(request, pk):
    booking = Booking.objects.get(id=pk)
    context = {
        'booking': booking,
    }
    return render(request, 'booking/booking_detail.html', context)

def booking_form(request):
    if request.method == 'GET':
        return render(request, 'booking/booking_form.html')
    else:
        room_number = request.POST.get('room_number')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        try:
            room = Room.objects.get(number=room_number)
        except ValueError: 
            return HttpResponse('Wrong Room Number', status=404)
        except Room.DoesNotExist:
            return HttpResponse("Room does not exist", status=404)
        
        booking = Booking.objects.create(
            room = room,
            user = request.user,
            start_time = start_time,
            end_time = end_time
        )
        return redirect('booking-detail', pk=booking.id)

            