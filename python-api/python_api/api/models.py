from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.JSONField()
    instructions = models.JSONField()
    image = models.URLField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.JSONField()

    def _str_(self):
        return self.name
