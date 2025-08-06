from rest_framework import serializers
from .models import Team
from users.models import CustomUser
from users.serializers import UserSerializer

class TeamSerializer(serializers.ModelSerializer):
    assigned_to_name = serializers.SerializerMethodField()

    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Team
        fields = [
            'id', 'name', 'assigned_to', 'assigned_to_name',
            'description', 'created_at'
        ]
        read_only_fields = ['assigned_to_name']

    def get_assigned_to_name(self, obj):
        return obj.assigned_to.name if obj.assigned_to and hasattr(obj.assigned_to, "name") else (
            obj.assigned_to.username if obj.assigned_to else None
        )


class TeamWithUsersSerializer(TeamSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta(TeamSerializer.Meta):
        fields = TeamSerializer.Meta.fields + ['users']


