from allauth.account.forms import SignupForm
from django import forms
from .models import UserProfile


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    phone_number = forms.CharField(max_length=20, required=True)

    def save(self, request):
        # Call the parent class's save method, which will save the user
        user = super(CustomSignupForm, self).save(request)

        # Create a UserProfile instance linked to the user
        UserProfile.objects.create(
            user=user,
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            phone_number=self.cleaned_data["phone_number"],
        )

        return user


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "phone_number"]
