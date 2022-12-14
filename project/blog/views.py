from django.shortcuts import render
from . models import New

def home(request):
    data = {
        'news': New.objects.all(),
        'title': 'Главная страница блога'
    }
    return render(request, 'blog/home.html', data)


def contacti(request):
    return render(request, 'blog/contacti.html', {
                      'title': 'Страница про нас.',
    })
