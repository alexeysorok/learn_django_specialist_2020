from django.shortcuts import render, get_object_or_404
from restful import restful
from django.http import HttpResponseRedirect
from django.urls import reverse

from ..forms import ProductModelForm
from ..models import Product


@restful
def create(request):

    product = Product()
    form = ProductModelForm(instance=product)

    return render(request, 'products/edit_product.html', locals())


@create.method('POST')
def create(request):

    product = Product()
    form = ProductModelForm(request.POST)

    if form.is_valid():
        product = form.save()
        return HttpResponseRedirect(reverse('products:show', args=[product.pk]))

        # return render(request, template_name="products/product.html", context=locals())
    else:
        print('Form no valid', form.is_valid())
        return render(request, template_name="products/edit_product.html", context=locals())
