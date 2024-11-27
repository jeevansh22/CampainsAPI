from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agents/', include('agents.urls')),
    path('campaigns/', include('campaigns.urls')),
    path('campaign-results/', include('campaign_results.urls')),
]
