from django import forms
from django.forms import ModelForm
from .models import Auction, User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
class AuctionForm(ModelForm):
    class Meta:
        model = Auction
        fields = ['name', 'category', 'description', 
                  'start_price', 'min_bid', 'picture']

class AuctionFormUpdate(ModelForm):
    class Meta:
        model = Auction
        fields = ['name', 'description']

def validate_bank_account(value):
    if not value.isdigit():
        raise ValidationError(("Bank account must contain only digits."))
    if len(value) != 26:
        raise ValidationError(("Bank account must be exactly 26 digits long."))


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    bank_account = forms.CharField(max_length=50, required=True, validators=[validate_bank_account])

    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=(""),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=(""),
    )

    username = forms.CharField(
        label=("Username"),
        max_length=150,
        help_text=(""),
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2', 'bank_account']