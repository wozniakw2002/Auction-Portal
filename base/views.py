from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Auction, Category, Comment, User
from .forms import AuctionForm, AuctionFormUpdate, RegistrationForm
from django.utils import timezone



def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
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
        
    context = {'page' : page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    page = 'register'
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')

    context = {'form': form, 'page': page}
    return render(request, 'base/login_register.html', context)



def home(request):
    
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    now = timezone.now()
    auctions = Auction.objects.filter(Q(category__name__icontains = query) |
                                      Q(name__icontains = query) |
                                      Q(description__icontains = query)).filter(duration__gt=now)
    categories = Category.objects.all()

    auction_count = auctions.count()


    context = {'auctions' : auctions, 'categories': categories, 'auction_count': auction_count}
    return render(request, 'base/home.html', context)

def auction(request, id):
    auction = Auction.objects.get(id = id)
    comments = auction.comment_set.all().order_by('-created')
    
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        bid_value = request.POST.get('bid')

        if comment_text:
            comment = Comment.objects.create(
                user=request.user,
                auction=auction,
                comment=comment_text
            )
            return redirect('auction', id=auction.id)

        if bid_value and int(bid_value) >= auction.min_bid + auction.current_price and int(bid_value) > auction.current_price and request.user != auction.host:
            if auction.duration <= timezone.now():
                return HttpResponse('This auction is not valid anymore')
            else:
                auction.current_price = int(bid_value)
                auction.last_bid_user = request.user
                auction.save()
                return redirect('auction', id=auction.id)

        else:
            return HttpResponse('Your bid value is not correct')
       

    context = {'auction': auction, 'comments' : comments}
    return render(request, 'base/auction.html', context)


@login_required(login_url='/login')
def yourProfile(request, pk):
    user = User.objects.get(id = pk)
    auctions = user.auction_set.all()
    won_auctions = Auction.objects.filter(has_ended=True).filter(last_bid_user_id = user.id)
    for auction in auctions:
        if auction.duration <= timezone.now():
            auction.has_ended = True
            auction.save()

    if request.user != user:
        return HttpResponse("You cannot see that profile.")
    auctions_active = auctions.filter(has_ended=False)
    auctions_disactive = auctions.filter(has_ended=True)
    print(auctions_active)
    context = {'user' : user, 'active': auctions_active, 
               'disactive': auctions_disactive, 'won_auctions': won_auctions}
    return render(request, 'base/your-profile.html', context)

@login_required(login_url='/login')
def createAuction(request):
    if request.method == 'POST':
        auction_form = AuctionForm(request.POST, request.FILES)

        if auction_form.is_valid():
            auction_form = auction_form.save(commit=False)
            auction_form.host = request.user
            auction_form.duration = request.POST['duration']

            auction_form.save()
            return redirect('home') 

    else:
        auction_form = AuctionForm()
    context = {'auction_form': auction_form}
    return render(request, 'base/auction_form.html', context)

@login_required(login_url='/login')
def updateAuction(request, pk):
    auction = Auction.objects.get(id = pk)
    form = AuctionFormUpdate(instance=auction)

    if request.user != auction.host:
        return HttpResponse('You are not allowd do do it!')

    if request.method == 'POST':
        form = AuctionFormUpdate(request.POST, instance=auction)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'auction_form': form}
    return render(request, 'base/auction_form_update.html', context)

@login_required(login_url='/login')
def deleteAuction(request, pk):
    auction = Auction.objects.get(id = pk)

    if request.user != auction.host:
        return HttpResponse('You are not allowd do do it!')

    if request.method == 'POST' and auction.current_price == auction.start_price:
        auction.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': auction})