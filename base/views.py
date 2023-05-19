from django.shortcuts import render, redirect
from .models import Todo
# from django.contrib.auth.models import User
from .forms import TodoForm, SignupForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
# from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def home(request):
    title = 'Tasks'
    user = request.user
    tasks = Todo.objects.filter(user=user) if user.is_authenticated else ''
    if request.method == 'GET':
        q = request.GET.get('q')
        if q == '1':
            tasks = tasks.filter(completed=True)
        elif q == '0':
            tasks = tasks.filter(completed=False)
        else:
            tasks = tasks
    now = timezone.now()

    context = {
        'title': title, 'tasks': tasks, 'now': now
    }
    return render(request, 'base/home.html', context)


def registerUser(request):
    page = 'register'
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)      
            # try:
            #     user = User.objects.get(user=user)
            #     if user:
            #         messages.error('This account exists already')
            # except:
            #     pass
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration!!!')
    form = SignupForm()

    context = {'form': form, 'page': page}
    return render(request, 'base/login-register.html', context)


def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'incorrect username or password')

    form = LoginForm()
    context = {'form': form, 'page': page}
    return render(request, 'base/login-register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def viewTask(request, pk):
    task = Todo.objects.get(id=pk)
    form = TodoForm(instance=task)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

    context = {'task': task, 'form': form}
    return render(request, 'base/task.html', context)


@login_required(login_url='login')
def addTask(request):
    form = TodoForm()
    if request.method == 'POST':
        user = request.user
        taskForm = TodoForm(request.POST)
        if taskForm.is_valid():
            todo = taskForm.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
        else:
            messages.error(request, 'Something went wrong!!!')
    context = {'form': form}
    return render(request, 'base/add_task.html', context)


def deleteTask(request, pk):
    task = Todo.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context = {'obj': f"{task} TASK"}
    return render(request, 'base/delete.html', context)


class UpdateTask(UpdateView):
    model = Todo
    # fields = '__all__'
    success_url = reverse_lazy('home')
    context_object_name = 'task'
    form_class = TodoForm
    template_name = 'base/update.html'

# def filterTask(request):
#     task

# def loginPage(request):
#     page = 'login'
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.error(request, 'incorrect username or password')
#     form = AuthenticationForm()
#     context = {'form': form, 'page': page}
#     return render(request, 'base/login-register.html', context)
