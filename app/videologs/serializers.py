from rest_framework import serializers
from .models import VideoLogs

class VideoLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoLogs
        fields="__all__"
