from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# from .


@login_required
def profile(request):
    """
    Display the users profile information
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    template = "profiles/profile.html"

    return render(request, template)
