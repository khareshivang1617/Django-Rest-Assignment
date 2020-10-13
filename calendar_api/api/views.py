from calendar_api.models import *
from . serializers import *

from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response

class eventListView(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        allEvents = event.objects.all().filter(user = request.user)
        serializer = eventSerializer(allEvents, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        
        data = request.data
        data["user"] = request.user.id
        serializer = eventSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


class eventDetailView(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=None):
        eventRequested = event.objects.get(id=id)
        serializer = eventSerializer(eventRequested)

        if serializer.data["user"] == request.user.id:
            return Response(serializer.data)

        else:
            return Response(status = 400)

    def put(self, request, id=None):
        eventRequested = event.objects.get(id=id)
        data = request.data
        data["user"] = request.user.id

        if eventRequested.user.id != request.user.id:
            return Response(status=400)

        serializer = eventSerializer(eventRequested, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)
    
    def delete(self, request, id=None):
        eventRequested = event.objects.get(id=id)
        
        if eventRequested.user.id != request.user.id:
            return Response(status=400)

        eventRequested.delete()
        return Response(status = 204)