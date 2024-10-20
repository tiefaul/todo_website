from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ListListView.as_view(), name='index'), # name parameter is used for the templates so they have something to point to
    path('list/<int:list_id>/', views.ItemListView.as_view(), name='list',),
    # CRUD patterns for ToDoLists
    path('list/add/', views.ListCreate.as_view(), name="list-add",),
    # CRUD patterns for ToDoItems
    path('list/<int:list_id>/item/add/', views.ItemCreate.as_view(), name='item-add',),
    path('list/<int:list_id>/item/<int:pk>/', views.ItemUpdate.as_view(), name='item-update',),
]