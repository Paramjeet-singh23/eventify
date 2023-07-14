from django.shortcuts import render

# Create your views here.
# views.py

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from rest_framework.views import APIView

# def register(request):
#     # Implement your user registration logic here
#     # ...

class LoginAPIView(APIView):

    def post(self, request):
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('success')  # Replace with your success URL
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('goodbye')  # Replace with your goodbye URL


class RegisterAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')

        if not email or not password or not first_name or not last_name:
            return Response(
                {'error': 'All fields must be filled.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()

        return Response(
            {
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            },
            status=status.HTTP_201_CREATED
        )

