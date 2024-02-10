from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('<str:shortlink>/', redirect_view, name='redirect'),
]

