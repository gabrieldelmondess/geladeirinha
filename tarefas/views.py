from django.shortcuts import render, redirect,get_object_or_404
from rest_framework import generics, status
from .serializers import *
from .models import *
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.contrib import messages
from rest_framework.views import APIView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse
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
            return redirect('tarefas:options-html')
        else:
            return render(request, self.template_name, {'serializer': serializer})

class DeleteTodo(View):
    def post(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return redirect('tarefas:list-todo')

class ConfirmDeleteTodo(View):
    template_name = 'confirm_delete.html'

    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        context = {
            'todo': todo,
        }
        return render(request, self.template_name, context)

def options(request):
    return render(request, 'options.html')



