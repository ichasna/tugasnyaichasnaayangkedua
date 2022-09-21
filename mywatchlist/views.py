from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import WatchList

def show_watchlist(request):
    data = WatchList.objects.all()
    context = {
    'nama': 'Syarifah Nur Amalia',
    'NPM' : '2106751272',
    'watchlist' : data,
    }
    return render(request, "mywatchlist.html", context)

def show_watchlist_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_watchlist_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_watchlist_html(request):
    data = WatchList.objects.all()
    context = {
    'nama': 'Syarifah Nur Amalia',
    'NPM' : '2106751272',
    'watchlist' : data,
    }
    return render(request, "mywatchlist.html", context)

# Create your views here.
