from django.shortcuts import render
from rest_framework import viewsets,generics
import pusher
from .models import Logs
from .serializers import LogsSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class LogsView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Logs.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=LogsSerializer


class LogNotification(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        pusher_client = pusher.Pusher(
        app_id='1985774',
        key='29e101e910ebcfc920cf',
        secret='7d0bd89bbbf022f90765',
        cluster='eu',
        ssl=True
        )
        pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
        return Response(status=status.HTTP_200_OK,data=[])