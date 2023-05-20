from django.db import models


class Points(models.Model):
    points = models.CharField(max_length=200)
    closest_pair = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
