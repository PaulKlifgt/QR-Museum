from django.db import models
import json

#раздел
class Section(models.Model):

    name = models.CharField(max_length=70)
    description = models.CharField(max_length=250)

#экспонат
class Exhibit(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=330)
    average_rank = models.FloatField(default=0.0)
    count_rank = models.IntegerField(default=0)
    section = models.ForeignKey(Section, null=True,  on_delete=models.SET_NULL)
    select_game = (
        (0, 'No game'),
        (1, 'Game 1'),
        (2, 'Game 2'),
        (3, 'Game 3')
    )
    type_game = models.IntegerField(default=0, choices=select_game)

    def toJSON(self):
        return {'id': self.id,
                'name': self.name, 
                'description': self.description, 
                'average_rank': self.average_rank, 
                'count_rank': self.count_rank,
                'type_game': self.type_game
                }
