from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from rest_framework.permissions import IsAuthenticated


class RegisterView(APIView):
    def post(self, request):
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        if not email or not password or not first_name or not last_name:
            return Response(
                {'error': 'Must include email, password, first_name, last_name.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()

        group, created = Group.objects.get_or_create(name='admin')
        group.user_set.add(user)

        return Response({'id': user.id, 'email': user.email}, status=status.HTTP_201_CREATED)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'user': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })
