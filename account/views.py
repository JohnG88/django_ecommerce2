import json
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_POST
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


# Create your views here.

def get_csrf(request):
    response = JsonResponse({"Info": "Success - Set CSRF cookie"})
    response['X-CSRFToken'] = get_token(request)
    return response

@require_POST
def loginView(request):
    data = json.loads(request.body)
    print(data)
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        return JsonResponse({"Info": "Username and password is needed"})

    user = authenticate(username=username, password=password)
    if user is None:
        return JsonResponse({"Info": "User does not exist."}, status=400)

    login(request, user)
    return JsonResponse({"Info":"User logged in successfully."})

class WhoAmIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        print(request.user.username)
        return JsonResponse({"username": request.user.username})




