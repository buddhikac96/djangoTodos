from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Todo
from .forms import TodoForm


# Create your views here.
class TodoList(ListView):
    model = Todo
    context_object_name = 'todos'


class TodoDetail(DetailView):
    model = Todo
    context_object_name = 'todo'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Todo, id=pk)


class TodoCreate(CreateView):
    model = Todo
    form_class = TodoForm

    def get_success_url(self):
        return reverse('todoapp:index')


class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Todo, id=pk)

    def get_success_url(self):
        return reverse('todoapp:index')


class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('todoapp:index')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Todo, id=pk)
