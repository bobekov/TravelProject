from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from travel_project.destination.models import Destination

UserModel = get_user_model()


class TestDestinationEdit(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='test@test.com',
            password='password1'
        )

        self.destination = Destination.objects.create(
            name="Angkor Wat",
            description="Angkor Wat is a Hindu-Buddhist temple.",
            country="Cambodia",
            city="",
            attractions="Bayon Temple",
            image="https://upload.wikimedia.org/wikipedia/commons/d/d4/20171126_Angkor_Wat_4712_DxO.jpg",
            best_time_to_visit="Summer",
            user=self.user
        )

        self.client.login(
            email='test@test.com',
            password='password1'
        )

    def test_destination_edit_success(self):
        updated_data = {
            'name': 'Angkor Wat',
            'description': 'Angkor Wat is a Hindu-Buddhist temple.',
            'country': 'Cambodia',
            'city': '',
            'attractions': 'Bayon Temple, Phnom Bakheng',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/d/d4/20171126_Angkor_Wat_4712_DxO.jpg',
            'best_time_to_visit': 'Autumn',
        }

        response = self.client.post(
            reverse('edit-destination', kwargs={'pk': self.destination.pk}),
            updated_data
        )

        self.destination.refresh_from_db()
        self.assertEqual(self.destination.attractions, 'Bayon Temple, Phnom Bakheng')
        self.assertEqual(self.destination.best_time_to_visit, 'Autumn')

        self.assertRedirects(response, reverse('details-destination'))

    def test_destination_edit_failure_invalid_data(self):
        invalid_data = {
            'name': 'Angkor Wat',
            'description': 'Angkor Wat is a Hindu-Buddhist temple.',
            'country': '',
            'city': '',
            'attractions': 'Bayon Temple, Phnom Bakheng',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/d/d4/20171126_Angkor_Wat_4712_DxO.jpg',
            'best_time_to_visit': 'Autumn',
        }

        response = self.client.post(
            reverse('edit-destination', kwargs={'pk': self.destination.pk}),
            invalid_data
        )

        self.assertEqual(response.status_code, 200)

        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('country', form.errors)
        self.assertIn('This field is required.', form.errors['country'])