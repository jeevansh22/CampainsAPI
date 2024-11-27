from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    voice_id = models.CharField(max_length=50, unique=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
