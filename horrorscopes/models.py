from django.db import models
from datetime import timezone
from django.contrib.auth.models import User



class Zodiac(models.Model):
    zodiac_name = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=50)
    insight = models.TextField()
    friendship = models.TextField()
    love = models.TextField()
    strengths = models.CharField(max_length=200)
    weakness = models.CharField(max_length=200)
    likes = models.CharField(max_length=200)
    dislikes = models.CharField(max_length=200)
    shade_of_insanity = models.CharField(max_length=200)
    element = models.ForeignKey('Element', on_delete=models.CASCADE)
    date_range = models.CharField(max_length=60, null=True, blank=True, default='')

    def __str__(self):
        return f'{self.zodiac_name}'

class Horoscope(models.Model):
    zodiac = models.ForeignKey(Zodiac, on_delete=models.CASCADE)
    post_date = models.DateField()
    horror = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.zodiac_name} - {self.post_date}'


class Tags(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.tag}'

class Element(models.Model):
    element_type = models.CharField(max_length=30)
    description = models.TextField()


    def __str__(self):
        return f'{self.element}'