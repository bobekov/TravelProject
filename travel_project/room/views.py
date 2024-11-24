from django.shortcuts import render, redirect, get_object_or_404
from travel_project.booking.models import BookingRoom
from travel_project.hotel.models import Hotel
from travel_project.room.forms import AddRoom
from travel_project.room.models import Room


def hotel_rooms(request, hotel_pk):
    search_query = request.GET.get('search', '')
    hotel = get_object_or_404(Hotel, pk=hotel_pk)

    if search_query:
        rooms = Room.objects.filter(hotel=hotel, room_type__icontains=search_query)
    else:
        rooms = Room.objects.filter(hotel=hotel)

    context = {
        'hotel': hotel,
        'rooms': rooms,
    }

    return render(request, 'room/rooms-hotel.html', context)


def add_new_room(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)

    if request.method == "POST":
        form = AddRoom(request.POST)

        if form.is_valid():
            room = form.save(commit=False)
            room.hotel = hotel
            room.user = request.user
            room.save()
            return redirect("hotel-rooms", hotel_pk=hotel.pk)
    else:
        form = AddRoom()

    context = {
        "form": form,
        "hotel": hotel
    }

    return render(request, 'room/add-room.html', context)


def edit_room(request, hotel_pk, room_pk):
    hotel = get_object_or_404(Hotel, pk=hotel_pk)
    room = get_object_or_404(Room, pk=room_pk, hotel=hotel)

    form = AddRoom(instance=room)

    if request.method == 'POST':
        form = AddRoom(request.POST, instance=room)
        if form.is_valid():
            room = form.save(commit=False)
            room.hotel = hotel
            room.save()
            return redirect('hotel-rooms', hotel_pk=hotel.pk)

    context = {
        'form': form,
        'room': room,
        'hotel': hotel,
    }
    return render(request, 'room/edit-room.html', context)


def delete_room(request, hotel_pk, room_pk):
    hotel = get_object_or_404(Hotel, pk=hotel_pk)
    room = get_object_or_404(Room, pk=room_pk, hotel=hotel)

    if request.method == 'POST':
        confirmation = request.POST.get('confirmation')

        if confirmation == 'Yes':
            room.delete()
            return redirect('hotel-rooms', hotel_pk=hotel.pk)
        else:
            return redirect('hotel-rooms', hotel_pk=hotel.pk)

    context = {
        'room': room,
        'hotel': hotel,
    }
    return render(request, 'room/delete-room.html', context)


def book_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    hotel = room.hotel

    if request.method == 'POST':
        confirmation = request.POST.get('confirmation')

        if confirmation == 'Yes':
            BookingRoom.objects.create(user=request.user, room=room)
            return redirect('hotel-bookings')
        else:
            return redirect('hotel-rooms', hotel_pk=hotel.pk)

    return render(request, 'room/book-room.html', {'room': room})
