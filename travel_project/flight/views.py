from django.shortcuts import render, redirect, get_object_or_404
from travel_project.booking.models import BookingFlight
from travel_project.flight.forms import AddFlight
from travel_project.flight.models import Flight


def details_flight(request):
    search_query = request.GET.get('search', '')

    if search_query:
        flights = Flight.objects.filter(flight_number__icontains=search_query)
    else:
        flights = Flight.objects.all()

    context = {
        'flights': flights
    }
    return render(request, 'flight/details-flight.html', context)


def add_new_flight(request):
    if request.method == "POST":
        form = AddFlight(request.POST)

        if form.is_valid():
            flight = form.save(commit=False)
            flight.user = request.user
            flight.save()
            return redirect("details-flight")
    else:
        form = AddFlight()

    context = {
        "form": form
    }

    return render(request, 'flight/add-flight.html', context)


def edit_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)

    form = AddFlight(instance=flight)

    if request.method == 'POST':
        form = AddFlight(request.POST, instance=flight)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.user = request.user
            flight.save()
            return redirect('details-flight')

    context = {
        'form': form,
        'flight': flight,
    }
    return render(request, 'flight/edit-flight.html', context)


def delete_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)

    if request.method == 'POST':
        confirmation = request.POST.get('confirmation')

        if confirmation == 'Yes':
            flight.delete()
            return redirect('details-flight')
        else:
            return redirect('details-flight')

    return render(request, 'flight/delete-flight.html', {'flight': flight})


def book_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)

    if request.method == 'POST':
        confirmation = request.POST.get('confirmation')

        if confirmation == 'Yes':
            BookingFlight.objects.create(user=request.user, flight=flight)
            return redirect('flight-bookings')
        else:
            return redirect('details-flight')

    return render(request, 'flight/book-flight.html', {'flight': flight})
