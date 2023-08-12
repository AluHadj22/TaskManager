from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy # импорт нужен, чтобы при каждом успешном выполнении, пользователя возвращало к задачам
from django.contrib.auth.views import LoginView # Импорт для возможности входа в система
from django.contrib.auth.mixins import LoginRequiredMixin # чтобы пользователь не могу получать доступ к листу по адресной строке без авторизации
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form: Any) -> HttpResponse:
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)





class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    #Точечная фильтрация для того, чтобы один пользователь не мог изменять задачи другого
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context
    
#Представление детальное
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


#Представление создания
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    # Он все делает за меня, нашел инфу на английском в одной статье!
    success_url = reverse_lazy('tasks') # вот для этого и нужен был импорт. Отправляю пользователя на task.html
    #Убираю имена пользователей, когда чеорвек добавляет задачу
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    

#Обновление и редактирование задачи
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


#Удалить задачу. Завтра добавь подтверждение для удаления
class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')






