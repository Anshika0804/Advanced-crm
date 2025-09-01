from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from leads.serializers import LeadSerializer, LeadDropdownSerializer
from leads.models import Lead

from permissions.permissions import (
    IsAgentOrAbove,
    IsTeamLeadOrAbove,
)
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response

from django.conf import settings
from leads.tasks import update_leads_count

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from notifications.models import Notification


# Create/List View
class LeadListCreateView(generics.ListCreateAPIView):
    serializer_class = LeadSerializer
    permission_classes = [IsAgentOrAbove]

    def get_queryset(self):
        user = self.request.user
        print("User:", user)
        print("Role:", user.role)

        if user.role == "admin":
            return Lead.objects.all()
        elif user.role in ["assigned_to", "team_lead"]:
            return Lead.objects.filter(team=user.team)
        elif user.role == "agent":
            return Lead.objects.filter(user=user)
        return Lead.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if not user.role:
            raise ValidationError("User has no role assigned.")
        lead = serializer.save(user=user)

        # update_leads_count.delay()  # Async
        update_leads_count() # instant sync (not async)

        #Trigger notification if assigned_to exists
        if lead.assigned_to:
            message = f"A new lead {lead.name} has been assigned to you."
            Notification.objects.create(user=lead.assigned_to, lead=lead, message=message)

            #Send Websocket Notification
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"user_{lead.assigned_to.id}",
                {
                    "type": "send_notification",
                    "message": {
                        "lead_id": lead.id, 
                        "message": message,
                    }
                }
            )



# Detail View (Retrieve/Update/Delete)
class LeadUpdateRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LeadSerializer
    permission_classes = [IsTeamLeadOrAbove]

    def get_queryset(self):
        user = self.request.user
        print("User (detail view):", user)
        print("Role (detail view):", user.role)

        if user.role == "agent":
            return Lead.objects.filter(user=user)
        elif user.role in ["manager", "admin", "team_lead"]:
            return Lead.objects.all()
        return Lead.objects.none()
    
    def perform_update(self, serializer):
        lead = serializer.save()

        #Check if lead has been assigned to someone
        if lead.assigned_to:
            message = f"You have been assigned lead '{lead.name}'."
            Notification.objects.create(user=lead.assigned_to, lead=lead, message=message)

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"user_{lead.assigned_to.id}",
                {
                    "type": "send_notification",
                    "message": {
                        "lead_id": lead.id,
                        "message": message,
                    },
                }
            )
    
    def perform_destroy(self, instance):
        # Delete the lead
        instance.delete()
        # Update Redis instantly
        update_leads_count()   


# Optional: List View used for extended table view on frontend (same serializer now)
class LeadExtendedListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.role == "admin":
            leads = Lead.objects.all()
        elif user.role in ["manager", "team_lead"]:
            leads = Lead.objects.filter(team=user.team)
        elif user.role == "agent":
            leads = Lead.objects.filter(user=user)
        else:
            leads = Lead.objects.none()

        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)


from leads.serializers import LeadWithContactsSerializer

class LeadWithContactsListView(generics.ListAPIView):
    queryset = Lead.objects.all().prefetch_related('contacts')
    serializer_class = LeadWithContactsSerializer


class LeadDropdownView(generics.ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadDropdownSerializer
