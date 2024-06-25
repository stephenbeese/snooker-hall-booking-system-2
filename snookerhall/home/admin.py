from django.contrib import admin
from .models import ClubDetails

@admin.register(ClubDetails)
class ClubDetails(admin.ModelAdmin):
    list_display = (
        'club_name',
        'logo',
        'description',
        'tagline',
        'primary_colour',
        'secondary_colour',
    )