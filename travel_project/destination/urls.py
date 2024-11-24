from django.urls import path, include
from travel_project.destination import views

urlpatterns = [
    path('details_destination/', views.details_destination, name='details-destination'),
    path('add_destination/', views.add_new_destination, name='add-destination'),
    path('<int:pk>/', include([
        path('edit_destination/', views.edit_destination, name='edit-destination'),
        path('delete_destination/', views.delete_destination, name='delete-destination'),
    ])),
]