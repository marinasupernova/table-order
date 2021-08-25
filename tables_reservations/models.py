from django.db import models

class Table(models.Model):
    number = models.IntegerField()
    num_of_seats = models.IntegerField()
    table_shape = models.IntegerField()
    coordinate_x = models.IntegerField()
    coordinate_y = models.IntegerField()
    size_width = models.IntegerField()
    size_length = models.IntegerField()


class Reservation(models.Model):
    date = models.DateField()
    table_number = models.IntegerField()


