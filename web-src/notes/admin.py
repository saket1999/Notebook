from django.contrib import admin
from .models import NoteBook, JSONField


class NotebookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'owner', 'created_at', 'updated_at']}),
        ('Info', {'fields': ['description']}),
        ('JSON', {'fields': ['data']}),
    ]
    list_display = ('name', 'owner', 'created_at')
    filter_horizontal = ()


admin.site.register(NoteBook, NotebookAdmin)
