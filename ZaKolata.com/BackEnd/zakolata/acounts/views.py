from django.shortcuts import render
from rest_framework import status, views
from rest_framework.response import Response
from .serializers import ClientSerializer


# Create your views here.

class ClientRegistrationView(views.APIView):
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
