from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from travel_project.country.forms import AddCountry
from travel_project.country.models import Country
from travel_project.country.serializers import CountrySerializer


@api_view(['GET'])
def details_country_rest(request):
    countries = Country.objects.all()

    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)


def details_country(request):
    search_query = request.GET.get('search', '')

    if search_query:
        countries = Country.objects.filter(name__icontains=search_query)
    else:
        countries = Country.objects.all()

    context = {
        'countries': countries
    }
    return render(request, 'country/details-country.html', context)


def add_new_country(request):
    if request.method == "POST":
        form = AddCountry(request.POST)

        if form.is_valid():
            country = form.save(commit=False)
            country.user = request.user
            country.save()
            return redirect("details-country")
    else:
        form = AddCountry()

    context = {
        "form": form
    }

    return render(request, 'country/add-country.html', context)


def edit_country(request, pk):
    country = get_object_or_404(Country, pk=pk)

    form = AddCountry(instance=country)

    if request.method == 'POST':
        form = AddCountry(request.POST, instance=country)
        if form.is_valid():
            country = form.save(commit=False)
            country.user = request.user
            country.save()
            return redirect('details-country')

    context = {
        'form': form,
        'country': country,
    }
    return render(request, 'country/edit-country.html', context)


def delete_country(request, pk):
    country = get_object_or_404(Country, pk=pk)

    if request.method == 'POST':
        confirmation = request.POST.get('confirmation')

        if confirmation == 'Yes':
            country.delete()
            return redirect('details-country')
        else:
            return redirect('details-country')

    return render(request, 'country/delete-country.html', {'country': country})