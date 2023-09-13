from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    template_name = 'todo_list.html'
    
    def get(self, request, *args, **kwargs):
        todos = Todo.objects.all()
        contexto = {
            'caminho_para_bootstrap_css': 'https://bootswatch.com/morph/bootstrap.min.css',
            'todos' : todos,
        }
        return render(request, self.template_name, contexto)


class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer

class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    template_name = "create.html"

    def post( self,request, *args, **kwargs):
        todos = Todo.objects.all()
        contexto = {
            'caminho_para_bootstrap_css': 'https://bootswatch.com/morph/bootstrap.min.css',
            'todos' : todos,
        }
        return render(request, self.template_name, contexto)

class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer



