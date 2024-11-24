from django.urls import path
from travel_project.booking import views

urlpatterns = [
    path('my_bookings/', views.my_bookings, name='my-bookings'),
    path('flight_bookings/', views.flight_bookings, name='flight-bookings'),
    path('hotel_bookings/', views.hotel_bookings, name='hotel-bookings'),
    path('delete_booking_flight/<int:pk>/', views.delete_booking_flight, name='delete-booking-flight'),
    path('delete_booking_room/<int:pk>/', views.delete_booking_room, name='delete-booking-room'),
]
