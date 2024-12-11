from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from travel_project.destination.models import Destination

UserModel = get_user_model()


class TestDestinationDelete(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='test@test.com',
            password='password'
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
            password='password'
        )

    def test_destination_delete_success(self):
        self.assertTrue(Destination.objects.filter(pk=self.destination.pk).exists())

        response = self.client.post(
            reverse('delete-destination', kwargs={'pk': self.destination.pk}),
            data={'confirmation': 'Yes'}
        )

        self.assertFalse(Destination.objects.filter(pk=self.destination.pk).exists())
        self.assertRedirects(response, reverse('details-destination'))

    def test_destination_delete_failure_invalid_method(self):
        self.assertTrue(Destination.objects.filter(pk=self.destination.pk).exists())

        response = self.client.get(
            reverse('delete-destination', kwargs={'pk': self.destination.pk})
        )

        self.assertTrue(Destination.objects.filter(pk=self.destination.pk).exists())
        self.assertEqual(response.status_code, 200)

    def test_destination_delete_failure_no_confirmation(self):
        self.assertTrue(Destination.objects.filter(pk=self.destination.pk).exists())

        response = self.client.post(
            reverse('delete-destination', kwargs={'pk': self.destination.pk}),
            data={'confirmation': ''}
        )

        self.assertTrue(Destination.objects.filter(pk=self.destination.pk).exists())
        self.assertRedirects(response, reverse('details-destination'))
