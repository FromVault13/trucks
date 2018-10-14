from django.db import models

class Samosval(models.Model):
    """describes all the characteristics of the machine"""
    board_num = models.CharField(max_length=50,
                                 primary_key=True,
                                 unique=True,
                                 )
    mark = models.CharField(max_length=50)
    max_cargo = models.IntegerField()
    current_cargo = models.IntegerField()

