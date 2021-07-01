from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from storeApp.models import Product
from .basket import Basket

# Create your views here.
def basket_summary(request):
    basket = Basket(request)
    return render(request, 'storeApp/basket/summary.html', {'basket': basket})

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        
        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        
        return response