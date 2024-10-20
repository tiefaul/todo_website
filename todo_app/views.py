from typing import Any
from django.views.generic import ListView, CreateView, UpdateView
from .models import ToDoList, ToDoItem
from django.urls import reverse

# Create your views here.

class ListListView(ListView):
    model = ToDoList
    template_name = 'todo_app/index.html'

class ItemListView(ListView):
    model = ToDoItem
    template_name = 'todo_app/todo_list.html'

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs['list_id'])
    
    def get_context_data(self): # type: ignore
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context
    
class ListCreate(CreateView):
    model = ToDoList
    fields = ["title"]
    
    def get_context_data(self): # type: ignore
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context
    
class ItemCreate(CreateView):
    model = ToDoItem
    fields = ["todo_list", "title", "description", "due_date",]

    def get_initial(self) -> dict[str, Any]:
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data
    
    def get_context_data(self): # type: ignore
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context
    
    def get_success_url(self) -> str:
        return reverse("list", args=[self.object.todo_list_id]) # type: ignore
    
class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = ["todo_list", "title", "description", "due_date"]

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list # type: ignore
        context["title"] = "Edit item"
        return context
    
    def get_success_url(self) -> str:
        return reverse("list", args=[self.object.todo_list_id]) # type: ignore