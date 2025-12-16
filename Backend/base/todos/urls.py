from django.urls import path
from todos.views import TodosView, todosListView
# from todos.views



urlpatterns = [
    path('todo', TodosView.as_view()),
    path('getAllTodos', todosListView.as_view()),
]