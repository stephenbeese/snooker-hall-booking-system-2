from .models import UserProfile


def profile_context_processors(request):
    profile = None
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            profile = None  # or handle as needed
    return {"profile": profile}
