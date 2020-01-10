from django.shortcuts import render, get_object_or_404

from ..models import Product


def show(request, id_product):
    product = get_object_or_404(Product, pk=id_product)
    tags = ','.join((tag.title for tag in product.tags.all()))
    return render(request, template_name="products/product.html", context=locals())
