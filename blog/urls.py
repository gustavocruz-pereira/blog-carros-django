from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artigos/', views.artigos, name='artigos'),
    path('mercadorias/', views.mercadorias, name='mercadorias'),
]
