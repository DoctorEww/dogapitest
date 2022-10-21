import datetime
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
import json

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

def validate_size(value):
    if value not in ["Tiny", "Small", "Medium", "Large"]:
        raise ValidationError(
            ('%(value)s is not "Tiny", "Small", "Medium", or "Large"'),
            params={'value': value},
        )

class Breed(models.Model):
    name = models.CharField(max_length=200)
    size = models.CharField(max_length =200, validators = [validate_size])
    friendliness = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    trainability = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    sheddingamount = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    exerciseneeds = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])

#Dog class for holding dog stuff
class Dog(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ])
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    favoritefood = models.CharField(max_length=200)
    favoritetoy = models.CharField(max_length=200)
