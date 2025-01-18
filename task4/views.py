from django.shortcuts import render
from django.http import HttpResponse

# Функция для создания общего контекста меню
def menu_context():
    return {
        'title': "Main page",
        'main': "Главная",
        'news': "Новости",
        'subscribes': "Подписки"
    }

# Представления
def menu(request):
    return render(request, 'fourth_task/menu.html', menu_context())

def news_page(request):
    context = menu_context()  # Общий контекст меню
    return render(request, 'fourth_task/news-page.html', context)

def subscribes_page(request):
    context = menu_context()  # Общий контекст меню
    context.update({
        'subscribe': 'Подписаться',
        'groups': ['4chan', 'Рифмы и панчи', 'Urban University'],
    })
    return render(request, 'fourth_task/subscribes-page.html', context)

def main_page(request):
    return render(request, 'fourth_task/main-page.html', menu_context())
