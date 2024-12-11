from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from travel_project.country.models import Country

UserModel = get_user_model()


class TestCountryDelete(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='test@test.com',
            password='password'
        )


        self.country = Country.objects.create(
            name="Peru",
            flag="https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Flag_of_Peru_%28state%29.svg/1200px-Flag_of_Peru_%28state%29.svg.png",
            continent="South America",
            description="Peru is famous for its iconic landmarks, including Machu Picchu.",
            capital="Lima",
            population="40",
            official_language="Spanish",
            currency="Sol",
            is_visited="False",
            user=self.user
        )

        self.client.login(
            email='test@test.com',
            password='password'
        )

    def test_country_delete_success(self):
        self.assertTrue(Country.objects.filter(pk=self.country.pk).exists())

        response = self.client.post(
            reverse('delete-country', kwargs={'pk': self.country.pk}),
            data={'confirmation': 'Yes'}
        )

        self.assertFalse(Country.objects.filter(pk=self.country.pk).exists())
        self.assertRedirects(response, reverse('details-country'))

    def test_country_delete_failure_invalid_method(self):
        self.assertTrue(Country.objects.filter(pk=self.country.pk).exists())

        response = self.client.get(
            reverse('delete-country', kwargs={'pk': self.country.pk})
        )

        self.assertTrue(Country.objects.filter(pk=self.country.pk).exists())
        self.assertEqual(response.status_code, 200)

    def test_country_delete_failure_no_confirmation(self):
        self.assertTrue(Country.objects.filter(pk=self.country.pk).exists())

        response = self.client.post(
            reverse('delete-country', kwargs={'pk': self.country.pk}),
            data={'confirmation': ''}
        )

        self.assertTrue(Country.objects.filter(pk=self.country.pk).exists())
        self.assertRedirects(response, reverse('details-country'))

