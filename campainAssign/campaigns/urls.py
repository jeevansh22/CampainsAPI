from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet

router = DefaultRouter()
router.register('', CampaignViewSet)

urlpatterns = router.urls
