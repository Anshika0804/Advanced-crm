from django.urls import path
from leads.views.campaign_views import CampaignListCreateView, CampaignRetrieveUpdateDestroyView

urlpatterns = [
    path('campaigns/', CampaignListCreateView.as_view(), name='campaign-list-create'),
    path('campaigns/<int:pk>/', CampaignRetrieveUpdateDestroyView.as_view(), name='campaign-detail-update-delete'),
]

