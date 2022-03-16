from django.test import SimpleTestCase
from django.urls import reverse, resolve
from journal.views import JournalListView, JournalCreateView, JournalUpdateView, JournalDeleteView


class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse('journallist')
        self.assertEquals(resolve(url).func.view_class, JournalListView)

    def test_create_url_resolves(self):
        url = reverse('createjournal')
        self.assertEquals(resolve(url).func.view_class, JournalCreateView)

    def test_update_url_resolves(self):
        url = reverse('updatejournal', args=['some-pk'])
        self.assertEquals(resolve(url).func.view_class, JournalUpdateView)
