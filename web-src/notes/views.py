from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.views.generic import TemplateView, View
from django.utils.crypto import get_random_string
from django.utils.html import strip_tags
from django.utils.timezone import now
from .models import NoteBook, Article,User
from .forms import NotebookCreationForm, NotebookChangeForm, ArticleCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
import random
from django.http import JsonResponse


def getList(request,uid):

     id = []
     name=[]
     user = User.objects.get(username = uid)
     try:
        notes = get_list_or_404(NoteBook, owner=user)
        for item in notes:
            id.append(item.id)
            name.append(item.name)
        x = {"id":id,"name":name}
        return JsonResponse(x)

     except:
         x = {"id": "id", "name": "name"}
         return JsonResponse(x)
     # x = {"id":["1","hello"],"name":["2","frjoi"]}
     # return JsonResponse(x)




class ProtectedView(LoginRequiredMixin, View):
    login_url = '/accounts/login'
    redirect_field_name = 'login'


class HomeView(TemplateView):

    def get(self, request):
        context = {'title': 'home'}
        return render(request, 'index.html', context=context)


# This Function defined below is used to generate a unique Notebook ID fo reach notebook during creation.

def create_notebook_id(size):
    uid = get_random_string(length=size)

    # check if notebook already exists if not, return id
    try:
        notebook = NoteBook.objects.get(id=uid)
    except:
        notebook = None

    if not notebook:
        return uid
    else:
        create_notebook_id(size)  # If uid already exists recreate uid



class NotebookCreationView(ProtectedView):

    def get(self, request):
        form = NotebookCreationForm()
        context = {'title': 'Create', 'form': form}
        return render(request, 'creation_form.html', context=context)

    def post(self, request):
        if request.method == 'POST':
            # clean data
            name = strip_tags(request.POST.get('name'))
            user = request.user
            about = request.POST.get('description')
            notebook_id = create_notebook_id(random.randint(5, 10))

            new_name = name if name else 'untitled'

            form = NotebookCreationForm()
            try:
                book = NoteBook.objects.create(id=notebook_id, name=new_name, owner=user, description=about)
                print('Notebook - {} created'.format(name))
                book.created_at = book.updated_at = now()
                book.save()
                context = {'title': 'Create', 'messages': ['Notebook created successfully'], 'form': form}
                return render(request, 'creation_form.html', context=context)

            except Exception as e:
                print(e)
                context = {'title': 'Create', 'messages': [e], 'form': form}
                return render(request, 'creation_form.html', context=context)

@csrf_exempt
def NotebookView(request,uid):
    # This Function is used to create new articles for Notebooks

     if request.method=='POST':

        notebook = NoteBook.objects.get(id=uid)
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(content)
        try:
            article = Article.objects.create(notebook=notebook, title=title, content=content)
            # print('Article - {} created'.format(content[:100]))

            article.created_at = now()
            article.save()
            return redirect('view_notebook', uid=uid)

        except Exception as e:
            context = {'title': 'Error', 'messages': [e]}
            return render(request, 'notebook.html', context=context)

     else:
         # def get(self, request, uid):
         try:
             notebook = get_object_or_404(NoteBook, id=uid, owner=request.user)
         except Exception as e:
             context = {'title': '404', 'messages': [e, 'OR, You do not own this notebook!']}
             return render(request, 'notebook.html', context=context)

         try:
             articles = get_list_or_404(Article, notebook=notebook)
         except:
             articles = None

         form = ArticleCreationForm()

         context = {'title': notebook.name, 'notebook': notebook, 'articles': articles,
                    'article_form': form} if articles is not None else {
             'title': notebook.name, 'notebook': notebook, 'article_form': form}
         return render(request, 'notebook.html', context=context)

class NotebookEditView(ProtectedView):

    def get(self, request, uid):
        try:
            notebook = get_object_or_404(NoteBook, id=uid, owner=request.user)
        except Exception as e:
            context = {'title': '404', 'messages': [e, 'OR, You do not own this notebook!']}
            return render(request, 'notebook.html', context=context)

        form = NotebookChangeForm(instance=notebook)

        context = {'title': notebook.name, 'notebook': notebook, 'form': form}
        return render(request, 'edit_notebook.html', context=context)

    def post(self, request, uid):
        try:
            notebook = get_object_or_404(NoteBook, id=uid, owner=request.user)
            notebook.name = request.POST.get('name')
            notebook.description = request.POST.get('description')
            notebook.updated_at = now()
            notebook.save()
        except Exception as e:
            return HttpResponse(e)
        return redirect('view_notebook', uid=notebook.id)







