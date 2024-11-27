from rest_framework import serializers
from .models import Campaign
from agents.serializers import AgentSerializer
from agents.models import Agent

class CampaignSerializer(serializers.ModelSerializer):
    agents = serializers.PrimaryKeyRelatedField(queryset=Agent.objects.all(), many=True)

    class Meta:
        model = Campaign
        fields = '__all__'
