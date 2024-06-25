from .models import ClubDetails

def club_details_processor(request):
    club_details = ClubDetails.objects.get_instance()
    return {'club_details': club_details}