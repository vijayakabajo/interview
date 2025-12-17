from django.shortcuts import render
from accounts.models import Users
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from accounts.helpers.jwt_helper import generate_access_token
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password, make_password


# Create your views here.
class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        response = {
            'status': True,
            'message': '',
            'data': None,
            'error': None
        }

        full_name = request.data.get('full_name')
        email = request.data.get('email')
        raw_password = request.data.get('password')

        if not all([full_name, email, raw_password]):
            response['status'] = False
            response['message'] = 'full_name, email and password required'
            return JsonResponse(response, status=400)

        if len(raw_password) < 8:
            response['status'] = False
            response['message'] = 'password must be at least 8 characters'
            return JsonResponse(response, status=400)

        email = email.lower().strip()

        if Users.objects.filter(email=email, deleted_at__isnull=True).exists():
            response['status'] = False
            response['message'] = 'email already exists'
            return JsonResponse(response, status=400)

        try:
            user = Users.objects.create(
                full_name=full_name,
                email=email,
                password=make_password(raw_password),
                is_active=True
            )
            response['message'] = 'User created successfully'
        except Exception as e:
            response['status'] = False
            response['message'] = 'error creating user'
            response['error'] = str(e)

        return JsonResponse(response)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        response = {
            'status': True,
            'message': 'success',
            'data': None,
            'error': None
        }

        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            response['status'] = False
            response['message'] = 'email and password required'
            return JsonResponse(response, status=400)

        try:
            user = Users.objects.get(
                email=email.lower().strip(),
                is_active=True,
                deleted_at__isnull=True
            )
        except Users.DoesNotExist:
            response['status'] = False
            response['message'] = 'invalid email or password'
            return JsonResponse(response, status=401)

        if not check_password(password, user.password):
            response['status'] = False
            response['message'] = 'invalid email or password'
            return JsonResponse(response, status=401)

        access_token = generate_access_token(user)

        response['data'] = {
            'access_token': access_token,
            'user': {
                'id': user.id,
                'email': user.email,
                'full_name': user.full_name
            }
        }

        return JsonResponse(response)

