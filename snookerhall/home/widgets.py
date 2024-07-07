from django import forms


class ColourPickerWidget(forms.TextInput):
    input_type = "color"
