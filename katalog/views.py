from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'nama': 'Syarifah Nur Amalia',
    'NPM' : '2106751272',
    'list_barang': data_barang_katalog,
    }
    return render(request, "katalog.html", context)