from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='reader_profile'),
    path('add-book/<int:book_id>/', views.add_to_profile, name='add_to_profile'),
]
