from rest_framework import serializers
from .models import CampaignResult

class CampaignResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignResult
        fields = '__all__'
