# leads/urls.py
from django.urls import path
from leads.views import (
    LeadListCreateView,
    LeadUpdateRetrieveDestroyView,
    LeadExtendedListView
)

urlpatterns = [
    path('', LeadListCreateView.as_view(), name='api-lead-list-create'),  
    path('<int:pk>/', LeadUpdateRetrieveDestroyView.as_view(), name='api-lead-detail-update-delete'),
    path('extended/', LeadExtendedListView.as_view(), name='lead-extended'),
]

