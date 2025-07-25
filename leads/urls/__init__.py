from django.urls import path
from leads.views import LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView

from django.urls import path, include

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('tickets/', include('leads.urls.ticket_urls')),
    path('notes/', include('leads.urls.note_urls')),
    path('attachments/', include('leads.urls.attachment_urls')),
    path('campaigns/', include('leads.urls.campaign_urls')),
]
