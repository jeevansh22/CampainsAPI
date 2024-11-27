from django.db import models
from campaigns.models import Campaign

class CampaignResult(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    cost = models.FloatField()
    outcome = models.CharField(max_length=100)
    call_duration = models.FloatField()
    recording = models.URLField(null=True, blank=True)
    summary = models.TextField()
    transcription = models.TextField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='results')

    def __str__(self):
        return self.name
