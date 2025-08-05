# contacts/urls.py

from django.urls import path
from leads.views import LeadWithContactsListView 
from .views import ContactDetailView, ContactCreateView

urlpatterns = [
    path('leads-with-contacts/', LeadWithContactsListView.as_view(), name='contacts-lead-list'),
    path('<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('', ContactCreateView.as_view(), name='contact-create'), 
]
