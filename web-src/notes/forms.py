from django import forms
from .models import NoteBook


class NotebookCreationForm(forms.ModelForm):

    class Meta:
        model = NoteBook
        fields = (
            'name', 'description', 'data',
        )
