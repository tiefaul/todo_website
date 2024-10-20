from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ListListView.as_view(), name='index'), # name parameter is used for the templates so they have something to point to
    path('list/<int:list_id>/', views.ItemListView.as_view(), name='list'),
]