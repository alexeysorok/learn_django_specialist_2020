from django.shortcuts import render

from ..models import Group


def groups(request):
    all_groups = Group.objects.all()
    return render(request, template_name="products/group_product.html", context=locals())
