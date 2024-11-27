from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .models import CampaignResult
from .serializers import CampaignResultSerializer

class CampaignResultViewSet(ModelViewSet):
    queryset = CampaignResult.objects.all()
    serializer_class = CampaignResultSerializer
    pagination_class = PageNumberPagination
