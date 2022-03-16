from django.test import SimpleTestCase
from journal.forms import JournalForm


class TestForms(SimpleTestCase):

    def test_journal_form_valid_data(self):
        form = JournalForm(data={
            'title': 'test1',
            'link': 'https:www.test1.com',
            'tags': ['test', 'test2'],
        })

        self.assertTrue(form.is_valid())

    def test_journal_form_no_data(self):
        form = JournalForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
