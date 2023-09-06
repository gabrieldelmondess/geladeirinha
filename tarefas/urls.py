from django.urls import path
from .views import *
urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view(), name='list-todo'),
    path('create', CreateTodo.as_view()),
    path('delete/<int:pk>', DeleteTodo.as_view())
]
