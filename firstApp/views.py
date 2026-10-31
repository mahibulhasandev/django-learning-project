from django.shortcuts import render
from django.http import HttpResponse
from .models import  multipleVarient, Store
from django.shortcuts import get_object_or_404
from .forms import MultipleItemForm, Store

from firstApp import views
# Create your views here.



# def home(request):
#     allItem = multipleVarient.objects.all()
#     return render(request, 'home.html', {'allItem': allItem})

# def about(request):
#     return render(request, 'about.html')


def home(request):
    allItem = multipleVarient.objects.all()
    return render(request, 'home.html', {'allItem': allItem})


def item(request):
    allItem = multipleVarient.objects.all()
    return render(request, 'item.html', {'allItem': allItem})

def item_details(request, item_id):
    item = get_object_or_404(multipleVarient, pk=item_id)
    return render(request, 'item_details.html', {'item': item})

def item_stores(request):
    stores = None
    if request.method == 'POST':
        form = MultipleItemForm(request.POST)
        if form.is_valid():
            item_variety = form.cleaned_data['item_varity']
            stores = Store.objects.filter(item_details=item_varity)
    else:
        form = MultipleItemForm()
    return render(request, 'item_stores.html', {'stores': stores, 'form': form})