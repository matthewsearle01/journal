from django.shortcuts import render
from .models import Journal
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import JournalForm
from taggit.models import Tag

# Create your views here.


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class JournalListView(TagMixin, ListView):
    model = Journal
    template_name = "journal/journal_list.html"
    context_object_name = "journal_list"


class TagListView(TagMixin, ListView):
    model = Journal
    template_name = "journal/journal_list.html"
    context_object_name = "journal_list"

    def get_queryset(self):
        return Journal.objects.filter(tags__slug=self.kwargs.get('tag_slug'))


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
