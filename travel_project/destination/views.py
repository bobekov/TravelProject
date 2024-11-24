from django.shortcuts import render, redirect, get_object_or_404
from travel_project.destination.forms import AddDestination
from travel_project.destination.models import Destination


def details_destination(request):
    search_query = request.GET.get('search', '')

    if search_query:
        destinations = Destination.objects.filter(name__icontains=search_query)
    else:
        destinations = Destination.objects.all()

    context = {
        'destinations': destinations
    }
    return render(request, 'destination/details-destination.html', context)


def add_new_destination(request):
    if request.method == "POST":
        form = AddDestination(request.POST)

        if form.is_valid():
            destination = form.save(commit=False)
            destination.user = request.user
            destination.save()
            return redirect("details-destination")
    else:
        form = AddDestination()

    context = {
        "form": form
    }

    return render(request, 'destination/add-destination.html', context)


def edit_destination(request, pk):
    destination = get_object_or_404(Destination, pk=pk)

    form = AddDestination(instance=destination)

    if request.method == 'POST':
        form = AddDestination(request.POST, instance=destination)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.user = request.user
            destination.save()
            return redirect('details-destination')

    context = {
        'form': form,
        'destination': destination,
    }
    return render(request, 'destination/edit-destination.html', context)


def delete_destination(request, pk):
    destination = get_object_or_404(Destination, pk=pk)

    if request.method == 'POST':
        confirmation = request.POST.get('confirmation')

        if confirmation == 'Yes':
            destination.delete()
            return redirect('details-destination')
        else:
            return redirect('details-destination')

    return render(request, 'destination/delete-destination.html', {'destination': destination})