from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister

# Список существующих пользователей
users = ['Will Smith', 'John Conor', 'Daenerys Targaryen']

# Регистрация через форму Django

def sign_up_by_django(request):
    info = {}  # Пустой словарь для передачи контекста
    if request.method == 'POST':
        form = UserRegister(request.POST, users=users)  # Передаем список пользователей в форму
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Записываем пользователя и выполняем дополнительные действия, если необходимо
            users.append(username)  # Добавляем пользователя в список
            return HttpResponse(f"Приветствуем, {username}!")
        else:
            # Если форма не прошла валидацию, выводим ошибки
            info['form'] = form  # Передаем форму с ошибками в шаблон
    else:
        form = UserRegister(users=users)  # Пустая форма

    info['form'] = form  # Передаем форму в шаблон
    return render(request, 'fifth_task/registration_page.html', info)

# Регистрация через HTML-форму
def sign_up_by_html(request):
    info = {}  # Контекст для передачи в шаблон
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()
        age = request.POST.get('age', '').strip()

        # Проверка на пустой ввод и обработка исключений
        try:
            age = int(age)  # Преобразуем возраст в число
        except ValueError:
            info['error'] = "Ошибка: возраст должен быть числом."
            return render(request, 'fifth_task/registration_page.html', info)

        # Проверка условий
        if username in users:
            info['error'] = "Ошибка: пользователь с таким именем уже существует."
        elif password != confirm_password:
            info['error'] = "Ошибка: пароли не совпадают."
        elif age < 18:
            info['error'] = "Ошибка: возраст должен быть не менее 18 лет."
        else:
            users.append(username)  # Добавляем пользователя
            return HttpResponse(f"Приветствуем, {username}!")

    return render(request, 'fifth_task/registration_page.html', info)
