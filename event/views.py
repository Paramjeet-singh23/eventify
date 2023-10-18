from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.db.models import Q
from .models import Event
from .serializers import EventSerializer


class EventView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            try:
                event = Event.objects.get(pk=pk)
                serializer = EventSerializer(event)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Event.DoesNotExist:
                return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        queryset = Event.objects.all()
        events = EventSerializer(queryset, many=True)

        return Response(events.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            # Save the new event to the database
            serializer.validated_data['organizer'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            event = Event.objects.get(event_id=pk)
        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        # Deserialize the request data using the EventSerializer and specify the instance
        serializer = EventSerializer(event, data=request.data, partial=True)

        if serializer.is_valid():
            # Ensure that the user making the patch request is the event organizer
            if request.user == event.organizer:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "You do not have permission to update this event"}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get query parameters for name and description
        name_query = request.query_params.get('name', '')
        description_query = request.query_params.get('description', '')

        queryset = Event.objects.filter(name__icontains=name_query, description__icontains=description_query)

        events = EventSerializer(queryset, many=True)
        return Response(events.data, status=status.HTTP_200_OK)
