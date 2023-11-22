from django.urls import path
from .views import *
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view(),name='detalhe'),
    path('', ListTodo.as_view(), name='list-todo'),
    path('create/', CreateTodo.as_view(), name='create_todo'),
    path('delete/<int:pk>', DeleteTodo.as_view(), name='delete-todo'),
    path('options/', options, name='options-html'),
    path('confirm-delete/<int:pk>', ConfirmDeleteTodo.as_view() , name= 'confirm-delete')
]