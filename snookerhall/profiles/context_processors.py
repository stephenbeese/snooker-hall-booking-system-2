# from django.shortcuts import get_object_or_404
# from .models import UserProfile


# def profile_context_processors(request):
#     profile = None
#     if request.user.is_authenticated:
#         profile = get_object_or_404(UserProfile, user=request.user)
#     context = {"profile": profile}
#     return context


from .models import UserProfile


def profile_context_processors(request):
    profile = None
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            profile = None  # or handle as needed
    return {"profile": profile}
