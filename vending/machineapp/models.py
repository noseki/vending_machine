from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    cost = models.IntegerField()

    def __str__(self):
       return "名前:" + self.name + " " + "説明:" + self.text + " " ;