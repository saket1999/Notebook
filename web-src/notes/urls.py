from django.urls import path
from .views import HomeView, NotebookCreationView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create', NotebookCreationView.as_view(), name='new_notebook'),
]
