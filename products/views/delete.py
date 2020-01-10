from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from ..models import Product


def delete(request, id_product):

    product = get_object_or_404(Product, pk=id_product)
    product.delete()
    return HttpResponseRedirect(reverse('products:index'))
