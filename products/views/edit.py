from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect

from restful import restful
from ..models import Product
from ..forms import ProductModelForm

import sys


@restful  # GET Method
def edit(request, id_product):
    product = get_object_or_404(Product, pk=id_product)

    # python_path = sys.path

    form = ProductModelForm(instance=product)

    return render(request, template_name="products/edit_product.html", context=locals())


@edit.method('POST')
def edit(request, id_product):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('products:index'))
    if not request.user.is_superuser:
        if not request.user.has_perm('product.change_product'):
            return HttpResponseRedirect(reverse('products:index'))

    product = get_object_or_404(Product, pk=id_product)

    form = ProductModelForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return render(request, template_name="products/product.html", context=locals())
    else:
        return render(request, template_name="products/edit_product.html", context=locals())


