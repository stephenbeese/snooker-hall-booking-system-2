from django.contrib import messages
from django import forms
from .models import Booking
from datetime import datetime, timedelta


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["table", "date", "start_time", "end_time", "duration"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "start_time": forms.TimeInput(attrs={"type": "time"}),
            "end_time": forms.TimeInput(attrs={"type": "time"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")
        duration = cleaned_data.get("duration")

        if not end_time and not duration:
            return messages.error("You must provide either an end time or a duration.")

        if end_time and duration:
            return messages.error(
                "You must provide either an end time or a duration, not both."
            )

        return cleaned_data
