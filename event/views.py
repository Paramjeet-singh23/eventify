from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from rest_framework import status
from rest_framework.views import APIView


class EventView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Event.objects.all()
        events = EventSerializer(queryset, many=True)

        return Response(events.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Deserialize the request data using the EventSerializer
        print(request.__dict__)
        # request.user
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            # Save the new event to the database
            serializer.validated_data['organizer'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
