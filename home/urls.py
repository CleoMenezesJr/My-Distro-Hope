from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view')
]
