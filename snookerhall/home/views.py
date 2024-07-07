from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ValidationError
from django.db import models
from .forms import ClubDetailsForm, OpeningHoursForm
from .models import ClubDetails, OpeningHours

import logging

logger = logging.getLogger(__name__)


def index(request):
    club_details = ClubDetails.objects.get_instance()
    return render(request, "home/index.html", {"club_details": club_details})


# Method to check if user is admin
def is_admin(user):
    return user.is_superuser or user.has_perm("home.change_clubdetails")


@login_required
@user_passes_test(is_admin)
def club_details_view(request):
    if request.method == "POST":
        form = ClubDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Club Details updated successfully")
            return redirect("home")
    else:
        form = ClubDetailsForm()

    return render(request, "home/club_details_form.html", {"form": form})


@login_required
@user_passes_test(is_admin)
def edit_club_details(request):
    club_details = ClubDetails.objects.get_instance()
    if request.method == "POST":
        form = ClubDetailsForm(request.POST, request.FILES, instance=club_details)
        if form.is_valid():
            form.save()
            messages.success(request, "Club Details updated successfully")
            return redirect("home")
        else:
            messages.error(request, "Failed to update. The form is not valid.")
    else:
        form = ClubDetailsForm(instance=club_details)
    return render(request, "home/edit_club_details.html", {"form": form})


@login_required
@user_passes_test(is_admin)
def manage_opening_hours(request):
    opening_hours = OpeningHours.objects.all().order_by("day_of_week")
    if request.method == "POST":
        form = OpeningHoursForm(request.POST)
        if form.is_valid():
            try:
                opening_time = form.save(commit=False)
                opening_time.save()
                messages.success(request, "Opening Hours Updated Successfully")
            except ValidationError as e:
                messages.error(request, f"Error: {e}")
        else:
            messages.error(request, "Form invalid, please try again.")
    else:
        form = OpeningHoursForm()

    context = {
        "form": form,
        "opening_hours": opening_hours,
    }
    return render(request, "home/manage_opening_hours.html", context)


@login_required
@user_passes_test(is_admin)
def edit_opening_hours(request, opening_hours_id):
    try:
        opening_hour = OpeningHours.objects.get(id=opening_hours_id)
    except OpeningHours.DoesNotExist:
        raise Http404("Opening hours not found")

    if request.method == "POST":
        form = OpeningHoursForm(request.POST, instance=opening_hour)
        if form.is_valid():
            form.save()
            messages.success(request, "Opening Hours Updated Successfully")
            return redirect("manage_opening_hours")  # Redirect to the list view
        else:
            messages.error(request, "Form invalid, please try again.")
    else:
        form = OpeningHoursForm(instance=opening_hour)

    context = {
        "form": form,
        "opening_hour": opening_hour,
    }
    return render(request, "home/edit_opening_hours.html", context)


@login_required
@user_passes_test(is_admin)
def dynamic_styles(request):
    """
    Handles dynamic styling from users choices
    data used in templates/dynamic_styles.css
    """
    club_details = ClubDetails.objects.get_instance()
    css = render_to_string("dynamic_styles.css", {"club_details": club_details})
    return HttpResponse(css, content_type="text/css")
