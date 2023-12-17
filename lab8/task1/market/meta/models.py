from django.db import models


class Feedback(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    speed_rate = models.IntegerField()
    comfort_rate = models.IntegerField()
    price_rate = models.IntegerField()
