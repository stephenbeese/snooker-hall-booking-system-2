from django.db import models
from django.contrib.auth.models import User
from tables.models import Table

from datetime import datetime, timedelta

import uuid


class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    duration = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    booking_reference = models.CharField(max_length=12, unique=True, editable=False)

    def save(self, *args, **kwargs):
        # Generate unique booking reference
        if not self.booking_reference:
            self.booking_reference = self.generate_unique_booking_reference()

        # Auto populate name and phone number from the user
        if not self.name or not self.phone_number:
            try:
                user_profile = self.user.userprofile  # Access user profile
                self.name = f"{user_profile.first_name} {user_profile.last_name}"
                self.phone_number = user_profile.phone_number
            except User.userprofile.RelatedObjectDoesNotExist:
                # Handle case where user has no profile
                self.name = "Unknown User"
                self.phone_number = "N/A"
        #     self.name = (
        #         self.user.userprofile.first_name + " " + self.user.userprofile.last_name
        #     )
        #     self.phone_number = self.userprofile.phone_number

        # Calculate duration or end_time if not provided
        if self.start_time and self.end_time:
            duration_timedelta = datetime.combine(
                self.date, self.end_time
            ) - datetime.combine(self.date, self.start_time)
            self.duration = duration_timedelta.total_seconds() / 3600
        elif self.start_time and self.duration:
            end_datetime = datetime.combine(self.date, self.start_time) + timedelta(
                hours=float(self.duration)
            )
            self.end_time = end_datetime.time()

        # Use table's price for calculating the booking price
        self.price = float(self.duration) * self.table.price

        super().save(*args, **kwargs)

    def generate_unique_booking_reference(self):
        """
        Generate a unique booking reference number.
        """
        return uuid.uuid4().hex[:12].upper()

    def __str__(self):
        return f"Booking by {self.name} on {self.date} from {self.start_time} to {self.end_time} at {self.table} - {self.booking_reference}"
