from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('club_details_form/', views.club_details_view, name="club_details"),
    path('edit-club-details/', views.edit_club_details, name='edit_club_details'),
    path('dynamic-styles.css', views.dynamic_styles, name='dynamic_styles'),  # URL for dynamic CSS
]
