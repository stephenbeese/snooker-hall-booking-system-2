from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import EditProfileForm

# from .


@login_required
def profile(request):
    """
    Display the users profile information
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    template = "profiles/profile.html"

    return render(request, template)


@login_required
def edit_profile(request):
    """
    Edit the user's profile information
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = EditProfileForm(instance=profile)

    context = {"form": form}
    template = "profiles/edit_profile.html"
    return render(request, template, context)
