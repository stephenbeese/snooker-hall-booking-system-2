from django.contrib import admin
from .models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "session_key", "created_at", "expires_at")
    readonly_fields = ("expires_at",)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        "table",
        "date",
        "start_time",
        "end_time",
        "duration",
        "game_type",
        "price",
        "created_at",
    )
