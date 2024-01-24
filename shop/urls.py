from django.urls import path
from .views import home
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),
    path('new/', Create, name='new'),
    path('list/', ListView.as_view(), name='list'),
    path('tur/', category_list, name='tur')
    
]

