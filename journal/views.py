from django.shortcuts import render
from .models import Journal
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import JournalForm
from pathlib import Path

# Create your views here.


class JournalListView(ListView):
    model = Journal
    template_name = "journal/journal_list.html"
    context_object_name = "journal_list"


class JournalCreateView(CreateView):
    model = Journal
    template_name = 'journal/create_journal_form.html'
    fields = ['title', 'link', 'tags', 'document']
    success_url = reverse_lazy('journallist')


class JournalUpdateView(UpdateView):
    model = Journal
    template_name = 'journal/update_journal_form.html'
    fields = ['title', 'link', 'tags', 'document']
    success_url = reverse_lazy('journallist')


class JournalDeleteView(DeleteView):
    model = Journal
    template_name = 'journal/delete_journal_form.html'
    success_url = reverse_lazy('journallist')


def upload(request):
    if request.method == "POST":
        form = JournalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("main:upload")
    form = JournalForm()
    journal = Journal.objects.all()
    return render(request=request, template_name="journal_list.html", context={'form': form, 'journal': journal})

# my_file = Path("/media/documents/file")
# if my_file.is_file():
#     show_link = True