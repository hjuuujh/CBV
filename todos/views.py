from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from todos.models import Todo
from django.urls import reverse
from django.views.generic import ListView, DetailView


# Create your views here.

class IndexView(ListView):
    template_name = "todos/index.html"
    def get_queryset(self):
        return Todo.objects.all().order_by('-pub_date')


class TodoDetail(DetailView):
    model = Todo    


def Insert(request):
    return render(request, 'todos/insert.html')

def db_insert(request):
    todo = Todo()
    todo.title = request.POST.get('title')
    todo.contents = request.POST.get('contents')
    todo.pub_date = request.POST.get('date')

    if(not todo.title or not todo.contents):
        context =  {'todo': todo, 'error_message': "빈칸 불가능 / 저장 안됨",}
        return render(request, 'todos/notnull.html',context)
    
    todo.save()

    return HttpResponseRedirect(reverse('todos:index', args=()))


def delete(request, id):
    try:
        selected_todo = get_object_or_404(Todo, pk=id)
    except (KeyError, Todo.DoesNotExist):
        context =  {'todo': todo, 'error_message': "Error",}
        return render(request, 'todos/detail.html',context)
    else:
        selected_todo.delete()
        return HttpResponseRedirect(reverse('todos:index', args=()))


def Update(request, id):
    todo = get_object_or_404(Todo, pk=id)
    context = {'id': todo.id}
    return render(request, 'todos/update.html',context)


def db_update(request, id):
    try:
        todo = get_object_or_404(Todo, pk=id)
    except (KeyError, Todo.DoesNotExist):
        context =  {'todo': todo, 'error_message': "Error",}
        return render(request, 'todos/detail.html',context)
    else:
        todo.id = id
        todo.title = request.POST.get('title')
        todo.contents = request.POST.get('contents')
        todo.pub_date = request.POST.get('date')
        todo.save()
        return HttpResponseRedirect(reverse('todos:index', args=()))