from django.urls import path, include
from travel_project.review import views

urlpatterns = [
    path('details_review/', views.DetailsReview.as_view(), name='details-review'),
    path('add_view/', views.AddNewReview.as_view(), name='add-review'),
    path('<int:pk>/', include([
        path('edit_review/', views.EditReview.as_view(), name='edit-review'),
        path('delete-review/', views.DeleteReview.as_view(), name='delete-review'),
    ]))
]