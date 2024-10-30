from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegisterForm, LoginForm
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registration_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/dashboard/')
    else:
        form = RegisterForm()
    return render(request, 'registration/registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Пользователь успешно аутентифицирован, перенаправляем его на защищенную страницу
            return redirect('/dashboard/')
        else:
            # Аутентификация не удалось, отображаем сообщение об ошибке
            return render(request, 'registration/login.html', {'error_message': 'Неверное имя пользователя или пароль'})
    else:
        form = LoginForm()
        # Если запрос не POST, отображаем страницу входа
        return render(request, 'registration/login.html', {'form': form})

def dashboard_view(request):
    # Проверяем аутентифицирован ли пользователь
    if request.user.is_authenticated:
        # Пользователь аутентифицирован, отображаем защищенную страницу
        return render(request, 'dashboard.html')
    else:
        # Пользователь не аутентифицирован, перенаправляем его на страницу входа
            return HttpResponseRedirect('/login/')

def logout_view(request):
    logout(request)
    # После выхода пользователя перенаправляем его на страницу входа
    return HttpResponseRedirect('/login/')

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

def user_view(request):
    if request.method == 'POST':
        # Получаем имя пользователя из формы
        username = request.POST.get('username')
        request.session['username'] = username
        return redirect('/profile/')

    # Если метод не POST, возвращаем форму или другое представление
    return render(request, 'user.html')

def set_cookie_view(request):
    html = HttpResponse('<h1>Hello</h1>')
    if request.COOKIES.get('visit_count'):
        visit_count = int(request.COOKIES.get('visit_count')) + 1
    else:
        visit_count = 1
    html.set_cookie('visit_count', str(visit_count))
    return html

def show_cookie_view(request):
    visit_count = request.COOKIES.get('visit_count', 0)
    return render(request, 'counter.html', {'visit_count': visit_count})

def delete_cookie_view(request):
    response = HttpResponseRedirect(reverse('index')) # Перенаправляем обратно на страницу профиля
    response.delete_cookie('visit_count') # Удаляем куки
    return response