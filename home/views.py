from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.utils.http import is_safe_url, urlunquote

from datetime import datetime

from .forms import LoginForm


# Create your views here.
def index(request):
    current_time = datetime.now()

    return render(request, template_name="home/index.html", context=locals())


def login_user(request):
    # Вход в систему
    form = LoginForm(request.POST)
    if form.is_valid():
        auth_login = form.cleaned_data['login']
        password = form.cleaned_data['password']
        user = authenticate(request, username=auth_login, password=password)
        if user is not None:
            login(request, user)

    # Ступай, откуда пришел
    # print('my_host:', request.get_host())
    way = request.META.get('HTTP_REFERER')
    if way:
        way = urlunquote(way)
        # print('way', way)
        # print(is_safe_url(way, request.get_host()))
    if not is_safe_url(way, request.get_host()):
        way = reverse('home:index')
    return HttpResponseRedirect(way)


def logout_user(request):
    pass
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))



