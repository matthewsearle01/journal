from django.test import TestCase
from journal.models import Journal


class TestModels(TestCase):

    def setUp(self):
        self.project1 = Journal.objects.create(
            id=1,
            title="Entry 1",
            link="http://test.com"
        )

    def test_entry_is_assigned_id_on_creation(self):
        self.assertEquals(self.project1.id, 1)
