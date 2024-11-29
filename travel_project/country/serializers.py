from rest_framework import serializers

from travel_project.country.models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        exclude = ('user', )