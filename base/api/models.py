from django.db import models

#раздел
class Section(models.Model):

    name = models.TextField(max_length=70)
    description = models.CharField(max_length=250)
    average_rank = models.FloatField()
    count_rank = models.IntegerField()
    type_game = models.IntegerField()

#экспонат
class Exhibit(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=330)
    average_rank = models.FloatField()
    count_rank = models.IntegerField()
    section = models.ForeignKey(Section, on_delete=models.SET_NULL)
