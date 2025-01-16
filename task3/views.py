from django.shortcuts import render
from django.template.defaultfilters import title


# Create your views here.
def main_page(request):
    title = "Main page"
    main = "Главная"
    news = "Новости"
    subscribes = "Подписки"
    context = {
        'title': title,
        'main': main,
        'news': news,
        "subscribes": subscribes
    }
    return render(request, 'third_task/main-page.html', context)

def news_page(request):
    return render(request, 'third_task/news-page.html')

def subscribes_page(request):
    subscribe = 'Подписаться'
    context = {
        'subscribe': subscribe,
    }
    return render(request, 'third_task/subscribes-page.html', context)