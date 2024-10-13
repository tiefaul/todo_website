from django.db import models

# Create your models here.

from django.utils import timezone
from django.urls import reverse

def one_week_hence() -> timezone.datetime:
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self) -> str:
        return reverse("list", args=[self.id]) # type: ignore
    
    def __str__(self) -> str:
        return self.title

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self) -> str:
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)] # type: ignore
        )
    
    def __str__(self) -> str:
        return f"{self.title}: due {self.due_date}"
    
    class Meta:
        ordering = ["due_date"]