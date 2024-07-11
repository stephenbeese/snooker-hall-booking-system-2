from django import forms
from .models import TableType, Table


class TableTypeForm(forms.ModelForm):
    class Meta:
        model = TableType
        fields = "__all__"


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = "__all__"
