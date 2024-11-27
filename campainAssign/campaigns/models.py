from django.db import models
from agents.models import Agent

class Campaign(models.Model):
    CAMPAIGN_TYPES = [('Inbound', 'Inbound'), ('Outbound', 'Outbound')]
    STATUS_CHOICES = [('Running', 'Running'), ('Paused', 'Paused'), ('Completed', 'Completed')]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CAMPAIGN_TYPES)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Running')
    agents = models.ManyToManyField(Agent)

    def __str__(self):
        return self.name
