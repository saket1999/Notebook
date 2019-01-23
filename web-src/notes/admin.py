from django.contrib import admin
from .models import NoteBook, Article


class NotebookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'owner', 'created_at']}),
        ('Info', {'fields': ['id', 'description', 'updated_at']}),
    ]
    list_display = ('name', 'owner', 'created_at')
    filter_horizontal = ()


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('info', {'fields': ['notebook', 'title', ]}),
        ('content', {'fields': ['content', 'created_at']}),
    ]
    list_display = ('title', 'notebook', 'created_at')
    filter_horizontal = ()


admin.site.register(NoteBook, NotebookAdmin)
admin.site.register(Article, ArticleAdmin)