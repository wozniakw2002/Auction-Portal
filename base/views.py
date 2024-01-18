from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Auction, Item, Category
from .forms import AuctionForm, ItemFormSet, AuctionFormUpdate


def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "User doesn't exist!" )
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is not valid.')
        
    context = {}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    auctions = Auction.objects.filter(Q(category__name__icontains = query) |
                                      Q(name__icontains = query) |
                                      Q(description__icontains = query))
    categories = Category.objects.all()

    auction_count = auctions.count()


    context = {'auctions' : auctions, 'categories': categories, 'auction_count': auction_count}
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

    if request.method == 'POST':
        form = AuctionFormUpdate(request.POST, instance=auction)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'auction_form': form}
    return render(request, 'base/auction_form.html', context)

def deleteAuction(request, pk):
    auction = Auction.objects.get(id = pk)

    if request.method == 'POST' and auction.current_price == auction.start_price:
        auction.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': auction})