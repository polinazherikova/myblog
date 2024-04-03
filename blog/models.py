from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=30)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Категорія"
        verbose_name_plural = "Категорії"

class Tags(models.Model):
    name=models.CharField(max_length=30)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Тег"
        verbose_name_plural = "Теги"

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=30,verbose_name="Заголовок")
    content=models.TextField(verbose_name="Опис")
    published_date=models.DateTimeField(auto_created=True,verbose_name="Дата")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Категорія")
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Автор")
    image=models.URLField(default="http://placehold.it/900x300")
    tags=models.ManyToManyField(Tags,verbose_name="Тег")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Пост"
        verbose_name_plural = "Пости"

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name="Коментар"
        verbose_name_plural = "Коментарі"

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name="Підписник"
        verbose_name_plural = "Підписники"

class PostPhoto(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост",related_name='images')
    image=models.ImageField(verbose_name="Картинка", upload_to="Post_Photos")

    class Meta:
        verbose_name="Картинка"
        verbose_name_plural = "Картинки"