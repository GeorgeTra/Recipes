from django import template
import recipes.views as views
from recipes.models import Category, TagRecipe

register = template.Library()


@register.inclusion_tag('recipes/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('recipes/list_tags.html')
def show_all_tags():
    return {'tags': TagRecipe.objects.all()}