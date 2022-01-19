from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .forms import LoginUserForm, TodoForm
from .models import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    form_class = TodoForm
    template_name = 'general/todo.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskList, self).form_valid(form)

    success_url = reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'general/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class CustomLoginView(LoginView):
    form_class = LoginUserForm
    template_name = 'general/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
