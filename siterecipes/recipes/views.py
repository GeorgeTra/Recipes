from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, \
    HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from django.urls import reverse

from .models import Recipes, Category, TagRecipe

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить рецепт', 'url_name': 'add_recipe'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Салат Цезарь с курицей', 'content': '''<h3>Описание приготовления:</h3> Давайте приготовим самое популярное блюдо в мире - Салат Цезарь. 
    Классический рецепт был придуман итальянским поваром Цезарем Кардини, который владел несколькими ресторанчиками в Мексиканском городе Тихуана. Салат Цезарь стал очень популярен по всему миру благодаря простоте приготовления и незабываемому вкусу. Делюсь классическим рецептом приготовления - теперь вы всегда будете знать как приготовить салат "Цезарь"! 
    На здоровье!''', 'is_published': True},
    {'id': 2, 'title': 'Салат зимний с колбасой', 'content': 'Рецепт зимнего салата', 'is_published': False},
    {'id': 3, 'title': 'Салат корейская морковь с курицей', 'content': 'Рецепт корейской моркови', 'is_published': True},
]


def index(request):
    recipes = Recipes.published.all()

    data = {'title': 'Главная страница',
            'menu': menu,
            'recipes': recipes,
            'cat_selected': 0,
            }
    return render(request, 'recipes/index.html', context=data)


def about(request):
    return render(request, 'recipes/about.html', {'title': 'О сайте', 'menu': menu})


def add_recipe(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_recipe(request, recipe_slug):
    recipe = get_object_or_404(Recipes, slug=recipe_slug)

    data = {'title': recipe.title,
            'menu': menu,
            'recipe': recipe,
            'cat_selected': 1,
            }

    return render(request, 'recipes/recipe.html', data)


def show_categories(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    recipes = Recipes.published.filter(cat_id=category.pk)

    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'recipes': recipes,
        'cat_selected': category.pk,
    }
    return render(request, 'recipes/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def show_tag_recipelist(request, tag_slug):
    tag = get_object_or_404(TagRecipe, slug=tag_slug)
    recipes = tag.tags.filter(is_published=Recipes.Status.PUBLISHED)

    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'recipes': recipes,
        'cat_selected': None,
    }

    return render(request, 'recipes/index.html', context=data)