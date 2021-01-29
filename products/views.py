from django.shortcuts import render
from .models import Product
from .forms import ProductForm
import logging


# Create your views here.

def product_create_view(request):
    """
    plain html form
    :param request:
    :return:
    """
    if request.method == 'POST':
        new_title = request.POST.get('title')
        Product.objects.create(title=new_title, description="blue", price=200.14, specs="Test")

    context = {}

    return render(request, 'products/create.html', context)


# def product_create_view(request):
"""
    with Django realted stuff.
"""


#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'products/create.html', context)


def product_detail_view(request, *args, **kwargs):
    # logging.basicConfig(level=logging.DEBUG)
    # logging.debug(request.user)
    obj = Product.objects.get(id=1)
    context = {
        'obj': obj
    }

    return render(request, 'products/detail.html', context)
