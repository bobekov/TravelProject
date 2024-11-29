from django.contrib import admin
from travel_project.country.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'continent', 'capital', 'official_language', 'is_visited']
    list_filter = ['is_visited']
