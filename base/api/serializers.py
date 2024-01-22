from rest_framework.serializers import ModelSerializer
from base.models import Auction

class AuctionSerializer(ModelSerializer):
    class Meta:
        model = Auction
        fields = '__all__'