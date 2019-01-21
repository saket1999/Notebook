from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, View
from django.utils.html import strip_tags
from django.utils.timezone import now
from .models import NoteBook
from .forms import NotebookCreationForm
import json


class HomeView(TemplateView):

    def get(self, request):
        context = {'title': 'home'}
        return render(request, 'index.html', context=context)


class NotebookCreationView(View):

    def get(self, request):
        form = NotebookCreationForm()
        context = {'title': 'Create', 'form': form}
        return render(request, 'creation_form.html', context=context)

    def post(self, request):
        if request.method == 'POST':
            # clean data
            name = strip_tags(request.POST.get('name'))
            user = request.user
            about = strip_tags(request.POST.get('description'))
            data = strip_tags(request.POST.get('data'))

            # check if notebook already exists if yes, rename it
            try:
                notebook = NoteBook.objects.get(name=name, owner=user)
            except:
                notebook = None
            new_name = name + ' (copy)' if notebook else name

            form = NotebookCreationForm()
            try:
                book = NoteBook.objects.create(name=new_name, owner=user, description=about, data=data)
                print('user created')
                book.created_at = book.updated_at = now()
                book.save()
                context = {'title': 'Create', 'messages': ['Notebook created successfully'], 'form':form}
                return render(request, 'creation_form.html', context=context)

            except Exception as e:
                print(e)
                context = {'title': 'Create', 'messages': e, 'form': form}
                return render(request, 'creation_form.html', context=context)

