from django.shortcuts import render
from .models import Cart, CartItem
from django.utils import timezone


def get_user_cart(request):
    """Get the cart for the current user or session."""
    if request.user.is_authenticated:
        return Cart.objects.filter(
            user=request.user, expires_at__gt=timezone.now()
        ).first()
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        return Cart.objects.filter(
            session_key=session_key, expires_at__gt=timezone.now()
        ).first()


def view_cart(request):
    cart = get_user_cart(request)
    cart_items = cart.items.all() if cart else []
    total_price = sum(item.price for item in cart_items)

    return render(
        request,
        "cart/view_cart.html",
        {
            "cart": cart,
            "cart_items": cart_items,
            "total_price": total_price,
        },
    )
