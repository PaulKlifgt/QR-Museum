from django.db import models
import json

#раздел
class Section(models.Model):

    name = models.CharField(max_length=70)
    description = models.CharField(max_length=250)


class Game(models.Model):

    name = models.CharField(max_length=100)

    select_template = (
        (1, 'Корабль'),
        (2, 'Археолог'),
        (3, 'Копатель')
    )
    template = models.IntegerField(default=1, choices=select_template)

#экспонат
class Exhibit(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=330)
    average_rank = models.FloatField(default=0.0)
    count_rank = models.IntegerField(default=0)
    section = models.ForeignKey(Section, null=True,  on_delete=models.SET_NULL)
    type_game = models.ForeignKey(Game, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='imgs')

    def toJSON(self):
        if self.type_game:
            return {'name': self.name, 
                    'description': self.description, 
                    'average_rank': self.average_rank, 
                    'count_rank': self.count_rank, 
                    'section': self.section.name,
                    'type_game': self.type_game.id}
        else:
            return {'name': self.name, 
                    'description': self.description, 
                    'average_rank': self.average_rank, 
                    'count_rank': self.count_rank, 
                    'section': self.section.name,
                    'type_game': self.type_game}


class Question(models.Model):

    name = models.CharField(max_length=100)
    correct = models.CharField(max_length=200)
    uncorrect_1 = models.CharField(max_length=200)
    uncorrect_2 = models.CharField(max_length=200)
    game = models.ForeignKey(Game, null=True, on_delete=models.SET_NULL)