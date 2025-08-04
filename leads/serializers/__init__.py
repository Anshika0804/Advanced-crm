# from rest_framework import serializers
# from leads.models import Lead  
# from .ticket_serializer import TicketSerializer
# from .note_serializer import NoteSerializer
# from .attachment_serializer import AttachmentSerializer
# from .campaign_serializer import CampaignSerializer

# __all__ = [
#     "TicketSerializer",
#     "LeadSerializer",
#     "NoteSerializer",
#     "AttachmentSerializer",
#     "CampaignSerializer",
# ]


# class LeadSerializer(serializers.ModelSerializer):
#     user_email = serializers.SerializerMethodField()
#     assigned_to_email = serializers.SerializerMethodField()

#     class Meta:
#         model = Lead
#         fields = '__all__' 
#         read_only_fields = ['user'] 

#     def get_user_email(self, obj):
#         return obj.user.email if obj.user else None

#     def get_assigned_to_email(self, obj):
#         return obj.assigned_to.email if obj.assigned_to else None
    
#     def get_team_name(self, obj):
#         return obj.team.name if obj.team else None




# # FRONTEND.....

# # leads/serializers.py

# from rest_framework import serializers
# from teams.models import Team 
# from leads.models import Lead

# class LeadExtendedSerializer(serializers.ModelSerializer):
#     assigned_by_name = serializers.SerializerMethodField()
#     assigned_to_name = serializers.SerializerMethodField()
#     team_name = serializers.SerializerMethodField()

#     team = serializers.SlugRelatedField(
#         slug_field='name',
#         queryset=Team.objects.all(),
#         allow_null=True,
#         required=False  # Optional team input
#     )

#     class Meta:
#         model = Lead
#         fields = [
#             "id", "name", "email", "phone_number", "status", 
#             "created_at", "updated_at", 
#             "assigned_by_name", "assigned_to_name", "team_name", "team"
#         ]

#     def get_assigned_by_name(self, obj):
#         return obj.user.name if obj.user and hasattr(obj.user, "name") else (obj.user.username if obj.user else None)

#     def get_assigned_to_name(self, obj):
#         return obj.assigned_to.name if obj.assigned_to and hasattr(obj.assigned_to, "name") else (obj.assigned_to.username if obj.assigned_to else None)

#     def get_team_name(self, obj):
#         return obj.team.name if obj.team else None

#     def create(self, validated_data):
#         # Auto-fill team if not provided
#         if not validated_data.get('team'):
#             assigned_to = validated_data.get('assigned_to')
#             user = self.context['request'].user

#             if assigned_to and assigned_to.team:
#                 validated_data['team'] = assigned_to.team
#             elif user and user.team:
#                 validated_data['team'] = user.team

#         return super().create(validated_data)

#     def update(self, instance, validated_data):
#         # Optional: Apply same logic during update if needed
#         if not validated_data.get('team'):
#             assigned_to = validated_data.get('assigned_to', instance.assigned_to)
#             user = self.context['request'].user

#             if assigned_to and assigned_to.team:
#                 validated_data['team'] = assigned_to.team
#             elif user and user.team:
#                 validated_data['team'] = user.team

#         return super().update(instance, validated_data)


# leads/serializers.py

from rest_framework import serializers
from teams.models import Team
from leads.models import Lead
from users.models import CustomUser  

class LeadSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()
    assigned_by_name = serializers.SerializerMethodField()
    assigned_to_name = serializers.SerializerMethodField()
    team_name = serializers.SerializerMethodField()

    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        allow_null=True,
        required=False
    )

    team = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Team.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Lead
        fields = [
            "id", "name", "email", "phone_number", "status",
            "user", "user_email", "assigned_to", "assigned_to_name", "assigned_by_name",
            "team", "team_name", "created_at", "updated_at"
        ]
        read_only_fields = ['user', 'user_email', 'assigned_by_name', 'assigned_to_name', 'team_name']

    def get_user_email(self, obj):
        return obj.user.email if obj.user else None

    def get_assigned_by_name(self, obj):
        return obj.user.name if obj.user and hasattr(obj.user, "name") else (obj.user.username if obj.user else None)

    def get_assigned_to_name(self, obj):
        return obj.assigned_to.name if obj.assigned_to and hasattr(obj.assigned_to, "name") else (obj.assigned_to.username if obj.assigned_to else None)

    def get_team_name(self, obj):
        return obj.team.name if obj.team else None

    def create(self, validated_data):
        if not validated_data.get('team'):
            assigned_to = validated_data.get('assigned_to')
            user = self.context['request'].user

            if assigned_to and assigned_to.team:
                validated_data['team'] = assigned_to.team
            elif user and user.team:
                validated_data['team'] = user.team

        return super().create(validated_data)

    def update(self, instance, validated_data):
        if not validated_data.get('team'):
            assigned_to = validated_data.get('assigned_to', instance.assigned_to)
            user = self.context['request'].user

            if assigned_to and assigned_to.team:
                validated_data['team'] = assigned_to.team
            elif user and user.team:
                validated_data['team'] = user.team

        return super().update(instance, validated_data)



from contacts.serializers import ContactSerializer

class LeadWithContactsSerializer(LeadSerializer):
    contacts = ContactSerializer(many=True, read_only=True)

    class Meta(LeadSerializer.Meta):
        fields = LeadSerializer.Meta.fields + ['contacts']
