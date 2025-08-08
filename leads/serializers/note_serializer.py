from rest_framework import serializers
from leads.models import Note

class NoteSerializer(serializers.ModelSerializer):
    lead_name = serializers.CharField(source='lead.name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.name', read_only=True)

    class Meta:
        model = Note
        fields = [
            'id',
            'description',
            'created_at',
            'created_by',
            'created_by_name',
            'lead',
            'lead_name',
            'ticket',
        ]
        read_only_fields = ['created_by', 'created_at']


    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
