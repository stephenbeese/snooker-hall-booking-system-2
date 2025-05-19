from django.shortcuts import render, redirect
from .forms import BookingForm
from tables.models import Table
from datetime import datetime, timedelta
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def book_table(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            # Get the cleaned data from the form
            game_type = form.cleaned_data["game_type"]
            date = form.cleaned_data["date"]
            start_time = form.cleaned_data["start_time"]
            duration = float(form.cleaned_data["duration"])

            # Find all available tables of the selected game type
            available_tables = Table.objects.filter(
                table_type=game_type, is_available=True
            )

            # If no tables are available, show an error
            if not available_tables.exists():
                messages.error(
                    request, "No available tables for the selected game type."
                )
                return render(request, "booking/book_table.html", {"form": form})

            # Calculate the end time for the booking
            end_time = (
                datetime.combine(date, start_time) + timedelta(hours=duration)
            ).time()

            # Check for overlapping bookings across all available tables
            overlapping_bookings = Booking.objects.filter(
                date=date,
                start_time__lt=end_time,
                end_time__gt=start_time,
            )

            # If all tables are booked during the selected time, show an error
            if overlapping_bookings.count() == available_tables.count():
                messages.error(
                    request,
                    "All available tables are booked during the selected time. Please choose a different time.",
                )
                return render(request, "booking/book_table.html", {"form": form})

            # Try to book an available table
            for table in available_tables:
                # Check if the table is already booked during the selected time
                if not overlapping_bookings.filter(table=table).exists():
                    booking = form.save(commit=False)
                    booking.table = table
                    booking.user = request.user
                    booking.save()
                    return redirect("booking_success")  # Redirect to the success page

            # If no available table could be booked (shouldn't reach here due to previous check)
            messages.error(
                request, "There was an issue with your booking. Please try again."
            )

        else:
            messages.error(
                request, "There was an issue with your booking. Please check the form."
            )

    else:
        form = BookingForm()

    return render(request, "booking/book_table.html", {"form": form})


@login_required
def booking_success(request):
    return render(request, "booking/booking_success.html")
