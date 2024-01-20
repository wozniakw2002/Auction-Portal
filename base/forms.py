from django.forms import ModelForm
from .models import Auction

class AuctionForm(ModelForm):
    class Meta:
        model = Auction
        fields = ['name', 'category', 'description', 
                  'start_price', 'min_bid', 'duration', 'picture']

class AuctionFormUpdate(ModelForm):
    class Meta:
        model = Auction
        fields = ['name', 'description']