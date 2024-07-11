from django import forms
from .models import ClubDetails, OpeningHours
from .widgets import ColourPickerWidget


# Define a form class for ClubDetails model
class ClubDetailsForm(forms.ModelForm):
    # Meta class to specify model and fields for the form
    class Meta:
        model = ClubDetails
        fields = "__all__"
        widgets = {
            "primary_colour": ColourPickerWidget(),
            "secondary_colour": ColourPickerWidget(),
            "header_colour": ColourPickerWidget(),
            "footer_colour": ColourPickerWidget(),
            "primary_text_colour": ColourPickerWidget(),
            "secondary_text_colour": ColourPickerWidget(),
            "header_text_colour": ColourPickerWidget(),
            "footer_text_colour": ColourPickerWidget(),
        }

    # Override the clean method to add custom validation
    def clean(self):
        cleaned_data = super().clean()  # Get the cleaned data from the for

        if ClubDetails.objects.exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("There can be only one ClubDetails instance")
        return cleaned_data


class OpeningHoursForm(forms.ModelForm):
    class Meta:
        model = OpeningHours
        fields = "__all__"
        widgets = {
            "opening_time": forms.TimeInput(attrs={"type": "time"}),
            "closing_time": forms.TimeInput(attrs={"type": "time"}),
        }
