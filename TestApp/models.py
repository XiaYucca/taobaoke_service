from django.db import models
from django.contrib import admin

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
#    timestamp = models.DateTimeField()
#    n_pingbacks = models.IntegerField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','body')


class Register(models.Model):
    userId = models.IntegerField()
    name = models.CharField(max_length = 150)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    headImg = models.ImageField(upload_to = 'TestApp/static/testApp/', default = 'TestApp/media/default.jpg')


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('userId','name','email','password','timestamp','headImg')

'''
class Entry(models.Model):
    blog = models.ForeignKey(BlogsPost)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(BlogsPost)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()'''


admin.site.register(BlogsPost,BlogPostAdmin)
admin.site.register(Register,RegisterAdmin)

import addUser

