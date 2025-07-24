from rest_framework import serializers
from leads.models import Attachment

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'
