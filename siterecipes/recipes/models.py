from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Recipes.Status.PUBLISHED)


class Recipes(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    cooking_steps = models.TextField(blank=True)
    cooking_time = models.CharField(blank=True, max_length=20)
    image = models.ImageField(blank=True)
    author = models.CharField(blank=True, max_length=40)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='recipes')
    tags = models.ManyToManyField('TagRecipe', blank=True, related_name='tags')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']
        indexes = [
            models.Index(fields=['-create_time'])
        ]

    def get_absolute_url(self):
        return reverse('recipe', kwargs={'recipe_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagRecipe(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})