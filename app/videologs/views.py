from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import VideoLogs
from .serializers import VideoLogsSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class VideoLogsView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=VideoLogs.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=VideoLogsSerializer


