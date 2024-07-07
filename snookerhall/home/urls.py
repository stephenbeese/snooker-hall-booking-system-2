from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("club_details_form/", views.club_details_view, name="club_details"),
    path("edit-club-details/", views.edit_club_details, name="edit_club_details"),
    path(
        "dynamic-styles.css", views.dynamic_styles, name="dynamic_styles"
    ),  # URL for dynamic CSS
    path("opening-hours/", views.manage_opening_hours, name="manage_opening_hours"),
    path(
        "edit_opening_hours/<int:opening_hours_id>/",
        views.edit_opening_hours,
        name="edit_opening_hours",
    ),
]
