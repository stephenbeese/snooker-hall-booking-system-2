from django.shortcuts import render, redirect
from .models import Booking, Table
from .forms import BookingForm
from django.contrib.auth.decorators import login_required


@login_required
def book_table(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect("booking_success")
    else:
        form = BookingForm()

    template = "booking/book_table.html"

    context = {"form": form}

    return render(request, template, context)


@login_required
def booking_success(request):
    return render(request, "booking/booking_success.html")
