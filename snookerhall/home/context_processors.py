from .models import ClubDetails, OpeningHours


def club_details_processor(request):
    club_details = ClubDetails.objects.get_instance()
    opening_hours = OpeningHours.objects.all().order_by("day_of_week")

    context = {
        "club_details": club_details,
        "opening_hours": opening_hours,
    }
    return context
