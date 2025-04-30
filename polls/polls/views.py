# polls/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # зберігаємо користувача
            login(request, user)  # автоматично входити після реєстрації
            return redirect('home')  # перенаправлення на головну сторінку
    else:
        form = RegistrationForm()  # якщо GET-запит, просто показуємо порожню форму

    return render(request, 'register.html', {'form': form})
