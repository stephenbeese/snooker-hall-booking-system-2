from django.contrib import admin
from .models import ClubDetails, OpeningHours


@admin.register(ClubDetails)
class ClubDetails(admin.ModelAdmin):
    list_display = (
        "club_name",
        "logo",
        "description",
        "tagline",
        "primary_colour",
        "secondary_colour",
    )


@admin.register(OpeningHours)
class OpeningHoursAdmin(admin.ModelAdmin):
    list_display = ["day_of_week", "opening_time", "closing_time"]
