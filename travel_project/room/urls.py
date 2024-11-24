from django.urls import path
from travel_project.room import views

urlpatterns = [
    path('hotel/<int:hotel_pk>/rooms/', views.hotel_rooms, name='hotel-rooms'),
    path('hotel/<int:pk>/add-room/', views.add_new_room, name='add-room'),
    path('<int:hotel_pk>/rooms/<int:room_pk>/edit/', views.edit_room, name='edit-room'),
    path('<int:hotel_pk>/rooms/<int:room_pk>/delete/', views.delete_room, name='delete-room'),
    path('room/<int:pk>/book/', views.book_room, name='book-room'),
]