from django.urls import path
from .views import LeadListCreateView, LeadUpdateRetrieveDestroyView

urlpatterns = [
    path('', LeadListCreateView.as_view(), name='lead-list-create'),
    path('<int:pk>/', LeadUpdateRetrieveDestroyView.as_view(), name='lead-detail'),
]
