
# Redirection de l'ApI

from django.urls import path
from . import views

# Redirection page web avec 'allusers/'
urlpatterns = [
    path('allusers/', views.UserListView.as_view(), name='user-list'),
]