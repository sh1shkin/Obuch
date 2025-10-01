from django.shortcuts import render
from store.models import *
def index(request):
    return render(request, 'store/index.html')

def catalog(request):
    context = {
        'title': "Каталог",
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),            
    }
    return render(request, 'store/catalog.html', context)