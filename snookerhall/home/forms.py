from django import forms
from .models import ClubDetails
from .widgets import ColourPickerWidget


class ClubDetailsForm(forms.ModelForm):
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

    def clean(self):
        cleaned_data = super().clean()
        if ClubDetails.objects.exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("There can be only one ClubDetails instance")
        return cleaned_data
