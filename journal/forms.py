from django import forms
from .models import Journal


# Create your forms here.
class JournalForm(forms.ModelForm):

    class Meta:
        model = Journal
        fields = ('title', 'link', 'tags', 'document')
