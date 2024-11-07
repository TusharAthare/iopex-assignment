from django.shortcuts import render
from rest_framework import generics
from users.models import User
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class RegisterView(APIView):
    """Creates user for specified email and name
    """
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"{e=}")
            return Response(data= {}, status=status.HTTP_400_BAD_REQUEST)