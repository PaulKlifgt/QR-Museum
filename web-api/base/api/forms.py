from django import forms
from . import models


class EditExhibitForm(forms.ModelForm):
    class Meta:
        model = models.Exhibit
        fields = ('name', 'description', 'section', 'type_game', 'image')
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'section': 'Раздел',
            'type_game': 'Игра',
            'image': 'Фото'
        }
        widgets = {
            'type_game': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(EditExhibitForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['description'].required = False
        self.fields['section'].required = False
        self.fields['type_game'].required = False
        self.fields['image'].required = False
        

class EditSectionForm(forms.ModelForm):
    class Meta:
        model = models.Section
        fields = ('name', 'description')
        labels = {
            'name': 'Имя',
            'description': 'Описание',
        }
        
    def __init__(self, *args, **kwargs):
        super(EditSectionForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['description'].required = False


class CreateExhibitForm(forms.ModelForm):
    class Meta:
        model = models.Exhibit
        fields = ('name', 'description', 'section', 'type_game', 'image')
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'section': 'Раздел',
            'type_game': 'Игра',
            'image': 'Фото'
        }
        widgets = {
            'type_game': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(CreateExhibitForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['type_game'].required = False
        self.fields['image'].required = False


class CreateSectionForm(forms.ModelForm):
    class Meta:
        model = models.Section
        fields = ('name', 'description')
        labels = {
            'name': 'Имя',
            'description': 'Описание',
        }    


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = models.Game
        fields = ('name', 'template')
        labels = {
            'name': 'Название',
            'template': 'Шаблон',
        }    


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ('name', 'correct', 'uncorrect_1', 'uncorrect_2', 'game')
        labels = {
            'name': 'Название',
            'correct': 'Правильный ответ',
            'uncorrect_1': 'Неправильный ответ',
            'uncorrect_2': 'Неправильный ответ',
            'game': 'Игра'
        }    