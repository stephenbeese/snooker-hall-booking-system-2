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

    def clean(self):
        cleaned_data = super().clean()
        table_number = cleaned_data.get("table_number")
        table_type = cleaned_data.get("table_type")

        if Table.objects.filter(
            table_number=table_number, table_type=table_type
        ).exists():
            raise forms.ValidationError(
                "A table with this number and type already exists."
            )

        return cleaned_data
