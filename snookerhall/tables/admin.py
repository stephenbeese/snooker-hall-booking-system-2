from django.contrib import admin
from .models import TableType, Table


@admin.register(TableType)
class TableTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("table_number", "table_type", "is_available")
    list_filter = ("table_type", "is_available")
