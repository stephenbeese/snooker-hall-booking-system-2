from django import forms
from .models import TableType


class TableTypeForm(forms.ModelForm):
    class Meta:
        model = TableType
        fields = "__all__"
