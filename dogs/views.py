from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from .models import Question, Dog, Breed
from django.template import loader
from django.http import Http404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dogs.serializers import BreedSerializer, DogSerializer

class BreedList(APIView):

    def get(self, request, format=None):
        #Might need to make pretty
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BreedDetail(APIView):
    """
    Retrieve, update or delete a Breed instance.
    """
    def get_object(self, pk):
        try:
            return Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Breed = self.get_object(pk)
        serializer = BreedSerializer(Breed)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Breed = self.get_object(pk)
        serializer = BreedSerializer(Breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Breed = self.get_object(pk)
        Breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DogList(APIView):

    def get(self, request, format=None):
        #Might need to make pretty
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DogDetail(APIView):
    """
    Retrieve, update or delete a Dog instance.
    """
    def get_object(self, pk):
        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Dog = self.get_object(pk)
        serializer = DogSerializer(Dog)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Dog = self.get_object(pk)
        serializer = DogSerializer(Dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Dog = self.get_object(pk)
        Dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)