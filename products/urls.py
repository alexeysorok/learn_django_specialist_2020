from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_product>/', views.show, name='show'),
    path('<int:id_product>/edit/', views.edit, name='edit'),
    path('<int:id_product>/delete/', views.delete, name='delete'),
    path('<int:id_product>/tags/', views.tags, name='tags'),
    path('<int:id_product>/<str:pk_tag>/delete/', views.delete_tag, name='delete_tag'),
    path('create/', views.create, name='create'),
    path('groups/', views.groups, name='groups')


]
