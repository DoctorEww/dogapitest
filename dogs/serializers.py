from rest_framework import serializers
from dogs.models import Breed, validate_size, Dog
from django.core.validators import MaxValueValidator, MinValueValidator

class BreedSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    size = serializers.CharField(max_length =200, validators = [validate_size])
    friendliness = serializers.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    trainability = serializers.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    sheddingamount = serializers.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    exerciseneeds = serializers.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Breed.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.friendliness = validated_data.get('friendliness', instance.friendliness)
        instance.trainability = validated_data.get('trainability', instance.trainability)
        instance.sheddingamount = validated_data.get('sheddingamount', instance.sheddingamount)
        instance.exerciseneeds = validated_data.get('exerciseneeds', instance.exerciseneeds)

        instance.save()
        return instance

class DogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    age = serializers.IntegerField(
        validators=[
            MinValueValidator(0)
        ])
    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())
    gender = serializers.CharField(max_length=200)
    color = serializers.CharField(max_length=200)
    favoritefood = serializers.CharField(max_length=200)
    favoritetoy = serializers.CharField(max_length=200)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Dog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.breed = validated_data.get('breed', instance.breed)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.color = validated_data.get('color', instance.color)
        instance.favoritefood = validated_data.get('favoritefood', instance.favoritefood)
        instance.favoritetoy = validated_data.get('favoritetoy', instance.favoritetoy)

        instance.save()
        return instance