from django.shortcuts import render, redirect, get_object_or_404
from travel_project.hotel.forms import AddHotel
from travel_project.hotel.models import Hotel


def details_hotel(request):
    search_query = request.GET.get('search', '')

    if search_query:
        hotels = Hotel.objects.filter(name__icontains=search_query)
    else:
        hotels = Hotel.objects.all()

    context = {
        'hotels': hotels
    }
    return render(request, 'hotel/details-hotel.html', context)


def add_new_hotel(request):
    if request.method == "POST":
        form = AddHotel(request.POST)

        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.user = request.user
            hotel.save()
            return redirect("details-hotel")
    else:
        form = AddHotel()

    context = {
        "form": form
    }

    return render(request, 'hotel/add-hotel.html', context)


def edit_hotel(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)

    form = AddHotel(instance=hotel)

    if request.method == 'POST':
        form = AddHotel(request.POST, instance=hotel)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.user = request.user
            hotel.save()
            return redirect('details-hotel')

    context = {
        'form': form,
        'hotel': hotel,
    }
    return render(request, 'hotel/edit-hotel.html', context)


def delete_hotel(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)

    if request.method == 'POST':
        confirmation = request.POST.get('confirmation')

        if confirmation == 'Yes':
            hotel.delete()
            return redirect('details-hotel')
        else:
            return redirect('details-hotel')

    return render(request, 'hotel/delete-hotel.html', {'hotel': hotel})


