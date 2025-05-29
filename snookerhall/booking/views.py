from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from tables.models import Table
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import Cart, CartItem
from django.utils import timezone


def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(
            user=request.user,
            defaults={"expires_at": timezone.now() + timedelta(minutes=15)},
        )
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(
            session_key=session_key,
            defaults={"expires_at": timezone.now() + timedelta(minutes=15)},
        )
    if created:
        cart.extend_expiration()
        cart.save()
    return cart


@login_required
def book_table(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data["game_type"]
            date = form.cleaned_data["date"]
            start_time = form.cleaned_data["start_time"]
            duration = float(form.cleaned_data["duration"])
            end_time = (
                datetime.combine(date, start_time) + timedelta(hours=duration)
            ).time()

            available_tables = Table.objects.filter(
                table_type=game_type, is_available=True
            )

            if not available_tables.exists():
                messages.error(
                    request, "No available tables for the selected game type."
                )
                return render(request, "booking/book_table.html", {"form": form})

            overlapping = Booking.objects.filter(
                date=date,
                start_time__lt=end_time,
                end_time__gt=start_time,
            )

            if overlapping.count() == available_tables.count():
                messages.error(request, "All tables are booked for that time.")
                return render(request, "booking/book_table.html", {"form": form})

            for table in available_tables:
                if not overlapping.filter(table=table).exists():
                    cart = get_or_create_cart(request)
                    cart_item = CartItem.objects.create(
                        cart=cart,
                        table=table,
                        date=date,
                        start_time=start_time,
                        duration=duration,
                        game_type=game_type,
                        price=table.price * duration,
                    )
                    cart_item.calculate_end_time()
                    cart_item.save()

                    messages.success(
                        request, f"Table {table.table_number} added to your basket."
                    )
                    return redirect("view_cart")  # ⬅️ Redirect to your cart view

            messages.error(request, "Unexpected error: no table could be added.")
        else:
            messages.error(request, "Please correct the form errors.")
    else:
        form = BookingForm()

    return render(request, "booking/book_table.html", {"form": form})


@login_required
def booking_success(request):
    return render(request, "booking/booking_success.html")
