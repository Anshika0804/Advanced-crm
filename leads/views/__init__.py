from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from leads.serializers import LeadSerializer

from leads.models import Lead
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .ticket_views import TicketViewSet
from .note_views import NoteViewSet
from .attachment_views import AttachmentViewSet
from .campaign_views import CampaignViewSet

# Create your views here.
class LeadListCreateView(generics.ListCreateAPIView):
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Lead.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LeadUpdateRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Lead.objects.filter(user=self.request.user)


class LeadListView(ListView):
    model = Lead
    template_name = "leads/lead_list.html"

class LeadDetailView(DetailView):
    model = Lead
    template_name = "leads/lead_detail.html"

class LeadCreateView(CreateView):
    model = Lead
    template_name = "leads/lead_form.html"
    fields = ['name', 'email', 'phone_number']
    template_name = "leads/lead_form.html"
    success_url = reverse_lazy('lead-list')

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class LeadUpdateView(UpdateView):
    model = Lead
    fields = ['name', 'email', 'phone_number']
    template_name = "leads/lead_form.html"
    success_url = reverse_lazy('lead-list')

class LeadDeleteView(DeleteView):
    model = Lead
    template_name = "leads/lead_confirm_delete.html"
    success_url = reverse_lazy('lead-list')