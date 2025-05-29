from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from tables.models import Table, TableType


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expires_at

    def extend_expiration(self, minutes=15):
        self.expires_at = timezone.now() + timedelta(minutes=minutes)
        self.save()

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.extend_expiration()
        super().save(*args, **kwargs)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    duration = models.DecimalField(max_digits=4, decimal_places=2)
    game_type = models.ForeignKey(TableType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_end_time(self):
        end_datetime = datetime.combine(self.date, self.start_time) + timedelta(
            hours=float(self.duration)
        )
        self.end_time = end_datetime.time()

    # def calculate_price(self):
    #     item_price = self.table.price * self.duration
    #     self.price = item_price

    def save(self, *args, **kwargs):
        if not self.end_time:
            self.calculate_end_time()

        # if not self.price:
        #     self.calculate_price()

        super().save(*args, **kwargs)
