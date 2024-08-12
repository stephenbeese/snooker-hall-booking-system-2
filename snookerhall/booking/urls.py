from django.urls import path
from . import views

urlpatterns = [
    path("book/", views.book_table, name="book_table"),
    path("booking-success/", views.booking_success, name="booking_success"),
]
