from rest_framework import serializers
from leads.models import Lead
from users.models import CustomUser
from contacts.serializers import ContactSerializer

class LeadSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()
    assigned_by_name = serializers.SerializerMethodField()
    assigned_to_name = serializers.SerializerMethodField()

    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Lead
        fields = [
            "id", "name", "email", "phone_number", "status",
            "user", "user_email", "assigned_to", "assigned_to_name",
            "assigned_by_name", "created_at", "updated_at"
        ]
        read_only_fields = ['user', 'user_email', 'assigned_by_name', 'assigned_to_name']

    def get_user_email(self, obj):
        return obj.user.email if obj.user else None

    def get_assigned_by_name(self, obj):
        return obj.user.name if obj.user and hasattr(obj.user, "name") else (obj.user.username if obj.user else None)

    def get_assigned_to_name(self, obj):
        return obj.assigned_to.name if obj.assigned_to and hasattr(obj.assigned_to, "name") else (obj.assigned_to.username if obj.assigned_to else None)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class LeadWithContactsSerializer(LeadSerializer):
    contacts = ContactSerializer(many=True, read_only=True)

    class Meta(LeadSerializer.Meta):
        fields = LeadSerializer.Meta.fields + ['contacts']
