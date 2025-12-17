from django.urls import path
from todos.views import TodosView, TodosListView
# from todos.views

urlpatterns = [
    path('todo', TodosView.as_view()),
    path('getAllTodos', TodosListView.as_view()),
]