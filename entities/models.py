from django.db import models
from entity_classes.models import EntityClass


class Entity(models.Model):
    classes = models.ManyToManyField(EntityClass, related_name='entities')
    name = models.CharField(max_length=200)
    social_name = models.CharField(max_length=200)
    document = models.CharField(max_length=100)

    def __str__(self):
        return f'{[entity_class.name for entity_class in self.classes.all()]} - {self.name}'
