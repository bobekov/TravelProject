from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from travel_project.country.models import Country

UserModel = get_user_model()


class TestCountryEdit(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='test@test.com',
            password='password1'
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
            password='password1'
        )

    def test_country_edit_success(self):
        updated_data = {
            'name': 'Peru',
            'flag': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Flag_of_Peru_%28state%29.svg/1200px-Flag_of_Peru_%28state%29.svg.png',
            'continent': 'South America',
            'description': 'Peru is famous for its iconic landmarks, including Machu Picchu.',
            'capital': 'Lima',
            'population': '50',
            'official_language': 'Spanish',
            'currency': 'Sol',
            'is_visited': 'True',
        }

        response = self.client.post(
            reverse('edit-country', kwargs={'pk': self.country.pk}),
            updated_data
        )

        self.country.refresh_from_db()
        self.assertEqual(self.country.population, 50)
        self.assertEqual(self.country.is_visited, True)

        self.assertRedirects(response, reverse('details-country'))

    def test_country_edit_failure_invalid_data(self):
        invalid_data = {
            'name': '',
            'flag': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Flag_of_Peru_%28state%29.svg/1200px-Flag_of_Peru_%28state%29.svg.png',
            'continent': 'South America',
            'description': 'Updated description for Peru.',
            'capital': 'Lima',
            'population': '50',
            'official_language': 'Spanish',
            'currency': 'Sol',
            'is_visited': 'True',
        }

        response = self.client.post(
            reverse('edit-country', kwargs={'pk': self.country.pk}),
            invalid_data
        )

        self.assertEqual(response.status_code, 200)

        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('name', form.errors)
        self.assertIn('This field is required.', form.errors['name'])

