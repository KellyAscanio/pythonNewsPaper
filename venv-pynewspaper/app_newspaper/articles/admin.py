from django.contrib import admin
from .models import Article, Comment
# Register your models here.

class CommentInline (admin.StackedInline): ##StackedInline= cada campo tiene su propia linea
    model= Comment
    extra= 0

class ArticleAdmin (admin.ModelAdmin): 
    inlines= [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
