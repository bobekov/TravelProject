from django.shortcuts import render, redirect, get_object_or_404
from travel_project.booking.models import BookingFlight, BookingRoom


def my_bookings(request):
    return render(request, 'booking/details-booking.html')


def flight_bookings(request):
    bookings = BookingFlight.objects.filter(user=request.user)

    filter_option = request.GET.get('filter', 'latest')
    if filter_option == 'oldest':
        bookings = bookings.order_by('booking_date')
    else:
        bookings = bookings.order_by('-booking_date')

    return render(request, 'booking/flight-booking.html', {'bookings': bookings})


def delete_booking_flight(request, pk):
    booking_flight = get_object_or_404(BookingFlight, pk=pk)

    if request.method == 'POST':
        confirmation = request.POST.get('confirmation')

        if confirmation == 'Yes':
            booking_flight.delete()
            return redirect('flight-bookings')
        else:
            return redirect('flight-bookings')

    return render(request, 'booking/cancel-flight-reservation.html', {'booking_flight': booking_flight})


def hotel_bookings(request):
    room_bookings = BookingRoom.objects.filter(user=request.user)

    filter_option = request.GET.get('filter', 'latest')
    if filter_option == 'oldest':
        room_bookings = room_bookings.order_by('booking_date')
    else:
        room_bookings = room_bookings.order_by('-booking_date')

    return render(request, 'booking/hotel-booking.html', {'room_bookings': room_bookings})


def delete_booking_room(request, pk):
    booking_room = get_object_or_404(BookingRoom, pk=pk)

    if request.method == 'POST':
        confirmation = request.POST.get('confirmation')

        if confirmation == 'Yes':
            booking_room.delete()
            return redirect('hotel-bookings')
        else:
            return redirect('hotel-bookings')

    return render(request, 'booking/cancel-hotel-reservation.html', {'booking_room': booking_room})