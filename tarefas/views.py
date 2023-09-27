from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.contrib import messages

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
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "create.html"

    def get(self, request):
        serializer = self.serializer_class()
        return render(request, self.template_name, {'serializer': serializer})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Tarefa registrada com sucesso!')
            return render(request, self.template_name,{'serializer': serializer, 'success_message': 'Tarefa gravada com sucesso!'})
        else:
            return render(request, self.template_name, {'serializer': serializer})
class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer



