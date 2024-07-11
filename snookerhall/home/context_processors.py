from .models import ClubDetails, OpeningHours


# Define a function to process and provide club details and opening hours
def club_details_processor(request):
    # Retrieve the single instance of ClubDetails
    club_details = ClubDetails.objects.get_instance()

    # Retrieve all instances of OpeningHours, ordered by the 'day_of_week' field
    opening_hours = OpeningHours.objects.all().order_by("day_of_week")

    # Create a context dictionary with club details and opening hours
    context = {
        "club_details": club_details,
        "opening_hours": opening_hours,
    }

    return context
