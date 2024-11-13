from django.urls import path, include
from . import views

urlpatterns = [
    path('todo-app/', views.ListListView.as_view(), name='index'), # name parameter is used for the templates so they have something to point to
    path('todo-app/list/<int:list_id>/', views.ItemListView.as_view(), name='list',),
    # CRUD patterns for ToDoLists
    path('todo-app/list/add/', views.ListCreate.as_view(), name="list-add",),
    path("todo-app/list/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete",),
    # CRUD patterns for ToDoItems
    path('todo-app/list/<int:list_id>/item/add/', views.ItemCreate.as_view(), name='item-add',),
    path('todo-app/list/<int:list_id>/item/<int:pk>/', views.ItemUpdate.as_view(), name='item-update',),
    path("todo-app/list/<int:list_id>/item/<int:pk>/delete/", views.ItemDelete.as_view(), name="item-delete",),
]