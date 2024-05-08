from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from car.serializers import contactUsSerializer
from rest_framework import status

# Create your views here.

@api_view(['POST'])
def create_car(request):
    print(request.data)
    serializer = contactUsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Details have been saved", status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
