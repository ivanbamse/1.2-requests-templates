from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def dish_view_implementation(request, dish):
    context = {'recipe': DATA[dish].copy()}
    quantity = float(request.GET.get('servings', 1))
    if quantity > 1:
        for item in context['recipe'].items():
            context['recipe'][item[0]] = item[1] * quantity
    return render(request, 'calculator/index.html', context)


def home_view(request):
    pages = {
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('buter')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, 'calculator/home.html', context)


def omlet_view(request):
    return dish_view_implementation(request, 'omlet')


def pasta_view(request):
    return dish_view_implementation(request, 'pasta')


def buter_view(request):
    return dish_view_implementation(request, 'buter')
