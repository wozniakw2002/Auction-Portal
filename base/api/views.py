from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Auction
from .serializers import AuctionSerializer

@api_view(['GET'])
def getRouts(request):
    routes = [
        'GET /api',
        'GET /api/auctions',
        'GET /api/auctions/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getAuctions(request):
    auctions = Auction.objects.all()
    serializer = AuctionSerializer(auctions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAuction(request, pk):
    auction = Auction.objects.get(id = pk)
    serializer = AuctionSerializer(auction, many=False)
    return Response(serializer.data)