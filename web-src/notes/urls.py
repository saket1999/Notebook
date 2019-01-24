from django.urls import path
from .views import HomeView, NotebookCreationView, NotebookView, NotebookEditView ,getList

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create', NotebookCreationView.as_view(), name='new_notebook'),
    path('view/<slug:uid>', NotebookView, name='view_notebook'),
    path('edit/<slug:uid>', NotebookEditView.as_view(), name='edit_notebook'),
    path('getList/<slug:uid>',getList,name='getList'),

]
