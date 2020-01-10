from django.shortcuts import render, get_object_or_404

from ..models import Product, Tag
from ..forms import TagListForm
from restful import restful
from django.db import connection
from textwrap import dedent


@restful
def tags(request, id_product):
    product = get_object_or_404(Product, pk=id_product)
    form = TagListForm()
    return render(request, 'products/tags.html', locals())


@tags.method('POST')
def tags(request, id_product):

    form = TagListForm(request.POST)
    if form.is_valid():
        tag_list = form.cleaned_data['tag_list']
        # product = get_object_or_404(Product, pk=id_product)
        tag_list = tag_list.split(',')
        tag_list = map(str.strip, tag_list)
        tag_list = map(str.lower, tag_list)
        with connection.cursor() as cursor:
            for pk_tag in tag_list:
                cursor.execute(dedent('''\
                insert into products_tag (title) 
                values (%s) 
                on conflict do nothing ;'''), [pk_tag])

                cursor.execute(dedent('''\
                select id from products_tag where title like %s;'''), [pk_tag])
                result = cursor.fetchall()
                tag_id = result[0]


                print('tag_id =', tag_id)

                cursor.execute(dedent('''\
                insert into products_product_tags (product_id, tag_id)
                values (%s, %s)
                on conflict do nothing ;'''), [id_product, tag_id])

    product = get_object_or_404(Product, pk=id_product)
    return render(request, 'products/tags.html', locals())


# @tags.method('POST')
# def tags_post_for_lamers(request, id_product):
#
#     form = TagListForm(request.POST)
#     if form.is_valid():
#         tag_list = form.cleaned_data['tag_list']
#         product = get_object_or_404(Product, pk=id_product)
#         for pk_tag in map(str.strip, tag_list.split(',')):
#             try:
#                 tag = Tag.objects.get(pk=pk_tag)
#             except Tag.DoesNotExist:
#                 tag = Tag(title=pk_tag)
#                 tag.save()
#         product.save()
#
#     return render(request, 'products/tags.html', locals())