from django.forms import ModelForm, inlineformset_factory
from .models import Auction, Item

class AuctionForm(ModelForm):
    class Meta:
        model = Auction
        fields = ['name', 'category', 'description', 'start_price', 'min_bid', 'duration']

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'picture']

ItemFormSet = inlineformset_factory(Auction, Item, form=ItemForm, extra=1, can_delete=False)

class AuctionFormUpdate(ModelForm):
    class Meta:
        model = Auction
        fields = ['name', 'description']