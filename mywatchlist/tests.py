from django.test import TestCase, Client
from django.urls import reverse
from mywatchlist.models import WatchList
import json

# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_show_watchlist(self):
        response = self.client.get(reverse("mywatchlist:show_watchlist"))
        self.assertEquals(response.status_code, 200)

    def test_show_watchlist_xml(self):
        response = self.client.get(reverse("mywatchlist:show_watchlist_xml"))
        self.assertEquals(response.status_code, 200)

    def test_show_watchlist_html(self):
        response = self.client.get(reverse("mywatchlist:show_watchlist_html"))
        self.assertEquals(response.status_code, 200)

    def test_show_watchlist_json(self):
        response = self.client.get(reverse("mywatchlist:show_watchlist_json"))
        self.assertEquals(response.status_code, 200)