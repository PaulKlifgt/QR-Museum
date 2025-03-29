from django import forms
from . import models

class EditExhibitForm(forms.ModelForm):
    class Meta:
        model = models.Exhibit
        fields = ('name', 'description', 'section')
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'section': 'Раздел'
        }
    def __init__(self, *args, **kwargs):
        super(EditExhibitForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['description'].required = False
        self.fields['section'].required = False
        

class EditSectionForm(forms.ModelForm):
    class Meta:
        model = models.Section
        fields = ('name', 'description', 'type_game')
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'type_game': 'Игра'
        }
        widgets = {
            'type_game': forms.Select(attrs={'class': 'form-control'})
        }
    def __init__(self, *args, **kwargs):
        super(EditSectionForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['description'].required = False
        self.fields['type_game'].required = False
