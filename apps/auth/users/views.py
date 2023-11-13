from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class ApiRoot(APIView):
    def get(self, request):
        return Response({"content": "Welcome to the root API!"}, status.HTTP_200_OK)

class SignUp(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_user = User.objects.filter(username=request.data['username']).first()
            new_user.set_password(request.data['password'])
            new_user.save()
            token = Token.objects.create(user=new_user)
            return Response({"token": token.key, "user":serializer.data}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
class SignIn(APIView):
    def post(self,request):
        user = get_object_or_404(User, username=request.data["username"])
        if not user.check_password(request.data["password"]):
            return Response({"detail": "Not Found"}, status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"value": token.key}, status.HTTP_202_ACCEPTED)