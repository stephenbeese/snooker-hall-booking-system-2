from django import forms
from .models import Booking
from tables.models import TableType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "date",
            "start_time",
            "duration",
            "game_type",
        ]  # game_type will be the TableType
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "start_time": forms.TimeInput(attrs={"type": "time"}),
            "duration": forms.NumberInput(
                attrs={"step": "0.5"}
            ),  # Optional: Adjust duration step
        }

    game_type = forms.ModelChoiceField(
        queryset=TableType.objects.all(),
        empty_label="Select Game Type",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Book Now"))

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        duration = cleaned_data.get("duration")
        game_type = cleaned_data.get("game_type")

        # Validation for game type and duration
        if not game_type:
            raise forms.ValidationError("Please select a game type.")

        if not duration:
            raise forms.ValidationError("Please specify the duration of your booking.")

        return cleaned_data
