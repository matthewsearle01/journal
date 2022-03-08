from django.urls import path
from . import views

urlpatterns = [
    path('journal/list', views.JournalListView.as_view(), name="journallist"),
    path('journal/journalcreate',
         views.JournalCreateView.as_view(),  name="createjournal"),
    path('journal/journalupdate/<pk>',
         views.JournalUpdateView.as_view(),  name="updatejournal"),
    path('journal/journaldelete/<pk>',
         views.JournalDeleteView.as_view(),  name="deletejournal"),
]
