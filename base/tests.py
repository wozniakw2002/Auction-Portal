from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from .views import home, createAuction, auction, updateAuction
from .models import Auction, Comment, Item
import json
class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_create_auction_url_is_resolved(self):
        url = reverse('create-auction')
        self.assertEqual(resolve(url).func, createAuction)

    def test_auction_url_is_resolved(self):
        url = reverse('auction', args=['pk'])
        self.assertEqual(resolve(url).func, auction)

    def test_update_auction_url_is_resolved(self):
        url = reverse('update-auction', args=['pk'])
        self.assertEqual(resolve(url).func, updateAuction)


class TestViews(TestCase):
    
    def test_home_get_GET(self):
        client = Client()

        response = client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/home.html')

