from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import connection
from textwrap import dedent

from ..models import Product
from ..models import Tag


def delete_tag_lamer(request, id_product, pk_tag):
    product = get_object_or_404(Product, pk=id_product)
    tag = get_object_or_404(Tag, pk=pk_tag)
    product.tags.remove(tag)
    product.save()
    return HttpResponseRedirect(reverse('products:tags', args=[id_product]))


def delete_tag(request, id_product, pk_tag):
    with connection.cursor() as cursor:
        cursor.execute(
            dedent('''\
            delete from products_product_tags 
            where product_id = %s and tag_id = %s;'''),
            [id_product, pk_tag]
                    )
    return HttpResponseRedirect(reverse('products:tags', args=[id_product]))