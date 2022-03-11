from django.shortcuts import render
from .models import Journal
# from .forms import Journal_Form
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.


class JournalListView(ListView):
    model = Journal
    template_name = "journal/journal_list.html"
    context_object_name = "journal_list"


class JournalCreateView(CreateView):
    model = Journal
    template_name = 'journal/create_journal_form.html'
    fields = ['title', 'link', 'tags']
    success_url = reverse_lazy('journallist')


class JournalUpdateView(UpdateView):
    model = Journal
    template_name = 'journal/update_journal_form.html'
    fields = ['title', 'link', 'tags']
    success_url = reverse_lazy('journallist')


class JournalDeleteView(DeleteView):
    model = Journal
    template_name = 'journal/delete_journal_form.html'
    success_url = reverse_lazy('journallist')


# def upload_file(request):
#     if request.method == 'POST':
#         form = Journal_Form(request.POST, request.FILES)
#         success_url = reverse_lazy('journallist')
#         if form.is_valid():
#             # file is saved
#             form.save()
#             return HttpResponseRedirect(success_url)
#     else:
#         form = ModelFormWithFileField()
#     return render(request, 'upload.html', {'form': form})
