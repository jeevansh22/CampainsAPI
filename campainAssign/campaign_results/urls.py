from rest_framework.routers import DefaultRouter
from .views import CampaignResultViewSet

router = DefaultRouter()
router.register('', CampaignResultViewSet)

urlpatterns = router.urls
