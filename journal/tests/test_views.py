from django.test import TestCase, Client
from django.urls import reverse
from journal.models import Journal


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('journallist')
        self.create_url = reverse('createjournal')
        self.update_url = reverse('updatejournal', args=[1])
        # mocking a journal entry to test JournalUpdateView
        self.entry1 = Journal.objects.create(id=1, title='entry1')
        self.entry2 = Journal.objects.create(id=2, title='entry2')
        self.delete_url = reverse('deletejournal', args=[2])

    def test_JournalListView_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'journal/journal_list.html')

    def test_JournalUpdateView_GET(self):
        response = self.client.get(self.update_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'journal/update_journal_form.html')

    def test_project_detail_POST_adds_new_entry(self):
        response = self.client.post(self.create_url, {
            'id': '1',
            'title': 'entry1',
            'link': 'https://entry1.com'
        })

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.entry1.title, 'entry1')
