from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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
    primary_colour = models.CharField(max_length=7, default="#FFFFFF")
    secondary_colour = models.CharField(max_length=7, default="#000000")
    header_colour = models.CharField(max_length=7, default="#FFFFFF")
    footer_colour = models.CharField(max_length=7, default="#FFFFFF")
    primary_text_colour = models.CharField(max_length=7, default="#FFFFFF")
    secondary_text_colour = models.CharField(max_length=7, default="#FFFFFF")
    header_text_colour = models.CharField(max_length=7, default="#FFFFFF")
    footer_text_colour = models.CharField(max_length=7, default="#FFFFFF")

    objects = ClubDetailsManager()

    def save(self, *args, **kwargs):
        # if an instance of this class exists you are unable to create a new one
        if not self.pk and ClubDetails.objects.exists():
            raise ValueError("There can be only one ClubDetails instance")
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.club_name)
