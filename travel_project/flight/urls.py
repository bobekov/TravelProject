from django.urls import path, include
from travel_project.flight import views

urlpatterns = [
    path('details_flight/', views.details_flight, name='details-flight'),
    path('add_flight/', views.add_new_flight, name='add-flight'),
    path('<int:pk>/', include([
        path('edit_flight/', views.edit_flight, name='edit-flight'),
        path('delete_flight/', views.delete_flight, name='delete-flight'),
        path('book_flight/', views.book_flight, name='book-flight'),
    ])),
]