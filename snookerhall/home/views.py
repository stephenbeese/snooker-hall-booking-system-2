from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ClubDetailsForm
from .models import ClubDetails

def index(request):
    club_details = ClubDetails.objects.get_instance()
    return render(request, 'home/index.html', {'club_details': club_details})

# Method to check if user is admin
def is_admin(user):
    return user.is_superuser or user.has_perm('home.change_clubdetails')


@login_required
@user_passes_test(is_admin)
def club_details_view(request):
    if request.method == 'POST':
        form = ClubDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClubDetailsForm()
    
    return render(request, 'home/club_details_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def edit_club_details(request):
    club_details = ClubDetails.objects.get_instance()
    if request.method == 'POST':
        form = ClubDetailsForm(request.POST, request.FILES, instance=club_details)
        if form.is_valid():
            form.save()
            return redirect('edit_club_details')
    else:
        form = ClubDetailsForm(instance=club_details)
    return render(request, 'home/edit_club_details.html', {'form': form})


def dynamic_styles(request):
    """
    Handles dynamic styling from users choices
    data used in templates/dynamic_styles.css
    """
    club_details = ClubDetails.objects.get_instance()
    css = render_to_string('dynamic_styles.css', {'club_details': club_details})
    return HttpResponse(css, content_type='text/css')