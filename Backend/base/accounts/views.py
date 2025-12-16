from django.shortcuts import render
from accounts.models import Users
from rest_framework.views import APIView
from django.http import JsonResponse


# Create your views here.
class SignupView(APIView):
    def post(self, request):

        response = {
            'status': True,
            'message': 'success'
        }

        password = request.data.get('password')
        full_name = request.data.get('full_name')
        email = request.data.get('email')

        if not password or not full_name or not email:
            response['status'] = False
            response['message'] = 'password, full_name and email are required'
            return JsonResponse(response)

        if Users.objects.filter(email=email).exists():
            response['status'] = False
            response['message'] = 'email already exists'
            return JsonResponse(response)

        Users.objects.create(
            password=password,
            full_name=full_name,
            email=email
        )

        return JsonResponse(response)
    
class LoginView(APIView):
    def post(self, request):
        response = {
            'status': True,
            'message': 'success'
        }

        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            response['status'] = False
            response['message'] = 'email and password are required'
            return JsonResponse(response)

        if not Users.objects.filter(email=email, password=password).exists():
            response['status'] = False
            response['message'] = 'invalid email or password'
            return JsonResponse(response)

        return JsonResponse(response)

        
