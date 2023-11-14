from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

def redirectRoot(request):
    return redirect('api-root')

class ApiRoot(APIView):
    def get(self, request):
        return Response({"content": "Welcome to the root API!"}, status.HTTP_200_OK)