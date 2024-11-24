from django.urls import path, include

from travel_project.hotel import views

urlpatterns = [
    path('details_hotel/', views.details_hotel, name='details-hotel'),
    path('add_hotel/', views.add_new_hotel, name='add-hotel'),
    path('<int:pk>/', include([
        path('edit_hotel/', views.edit_hotel, name='edit-hotel'),
        path('delete_hotel/', views.delete_hotel, name='delete-hotel'),
    ])),
]