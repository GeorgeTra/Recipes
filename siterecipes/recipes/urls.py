from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('recipe/<slug:recipe_slug>/', views.show_recipe, name='recipe'),
    path('category/<slug:cat_slug>/', views.show_categories, name='category'),
    path('tag/<slug:tag_slug>/', views.show_tag_recipelist, name='tag'),
]