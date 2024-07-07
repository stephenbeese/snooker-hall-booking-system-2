from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class ClubDetailsManager(models.Manager):
    """
    Ensures only one instance can be made
    """

    def get_instance(self):
        if self.exists():
            return self.get()
        return self.create()


class ClubDetails(models.Model):
    """
    Model to store club information
    """

    club_name = models.CharField(max_length=30)
    logo = models.ImageField(null=True, blank=True)
    home_image = models.ImageField(null=True, blank=True)
    address_line1 = models.CharField(max_length=100, blank=True)
    address_line2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=8, blank=True)
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True)
    display_logo = models.BooleanField(default=False)
    display_club_name = models.BooleanField(default=True)
    description = models.TextField()
    tagline = models.TextField()
    primary_colour = models.CharField(max_length=7, default="#ddd7d4")
    secondary_colour = models.CharField(max_length=7, default="#df0020")
    header_colour = models.CharField(max_length=7, default="#0e0e14")
    footer_colour = models.CharField(max_length=7, default="#0e0e14")
    primary_text_colour = models.CharField(max_length=7, default="#0e0e14")
    secondary_text_colour = models.CharField(max_length=7, default="#ddd7d4")
    header_text_colour = models.CharField(max_length=7, default="#ddd7d4")
    footer_text_colour = models.CharField(max_length=7, default="#ddd7d4")

    objects = ClubDetailsManager()

    def save(self, *args, **kwargs):
        # if an instance of this class exists you are unable to create a new one
        if not self.pk and ClubDetails.objects.exists():
            raise ValueError("There can be only one ClubDetails instance")
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.club_name)


class OpeningHours(models.Model):
    """
    Model to store club opening hours for each day of the week
    """

    DAY_CHOICES = (
        (1, _("Monday")),
        (2, _("Tuesday")),
        (3, _("Wednesday")),
        (4, _("Thursday")),
        (5, _("Friday")),
        (6, _("Saturday")),
        (7, _("Sunday")),
    )
    day_of_week = models.IntegerField(choices=DAY_CHOICES, unique=True)
    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)
    closed = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Opening Time")
        verbose_name_plural = _("Opening Times")

    def __str__(self):
        return f"{self.get_day_of_week_display()} - {self.opening_time} to {self.closing_time}"
