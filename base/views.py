from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Auction, Item
from .forms import AuctionForm, ItemFormSet, AuctionFormUpdate


def home(request):
    auctions = Auction.objects.all()
    context = {'auctions' : auctions}
    return render(request, 'base/home.html', context)

def auction(request, id):
    auction = Auction.objects.get(id = id)
    context = {'auction': auction}
    return render(request, 'base/auction.html', context)

def createAuction(request):
    if request.method == 'POST':
        auction_form = AuctionForm(request.POST)
        item_formset = ItemFormSet(request.POST, request.FILES, instance=Auction())

        if auction_form.is_valid() and item_formset.is_valid():
            auction = auction_form.save()
            item_formset.instance = auction
            item_formset.save()

            return redirect('home')  # Przekieruj gdziekolwiek chcesz po utworzeniu aukcji

    else:
        auction_form = AuctionForm()
        item_formset = ItemFormSet(instance=Auction())

    return render(request, 'base/auction_form.html', {'auction_form': auction_form, 'item_formset': item_formset})


def updateAuction(request, pk):
    auction = Auction.objects.get(id = pk)
    form = AuctionFormUpdate(instance=auction)
    context = {'auction_form': form}
    return render(request, 'base/auction_form.html', context)