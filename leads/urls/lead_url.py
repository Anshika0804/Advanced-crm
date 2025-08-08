from django.urls import path, include
from leads.views.lead_views import (
    LeadListCreateView,
    LeadUpdateRetrieveDestroyView,
    LeadExtendedListView, LeadDropdownView
)

urlpatterns = [
    path('', LeadListCreateView.as_view(), name='api-lead-list-create'),
    path('<int:pk>/', LeadUpdateRetrieveDestroyView.as_view(), name='api-lead-detail-update-delete'),
    path('extended/', LeadExtendedListView.as_view(), name='lead-extended'),
    path('dropdown/', LeadDropdownView.as_view(), name='lead-dropdown'),

    path("", include("leads.urls.ticket_urls")),
    path("", include("leads.urls.note_urls")),
    path("", include("leads.urls.attachment_urls")),
    path("", include("leads.urls.campaign_urls")),
]
