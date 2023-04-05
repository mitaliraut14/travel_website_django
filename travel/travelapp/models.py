from django.db import models

# Create your models here.

class Places(models.Model):
    State=models.CharField(max_length=100)
    Package=models.IntegerField()
    Days=models.IntegerField()
    Image=models.CharField(max_length=1000)
    Start_date=models.DateField()
    End_date=models.DateField()
    Hotel_name=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    created_on=models.DateTimeField()


class Book(models.Model):
    pid=models.IntegerField()
    uid=models.IntegerField()
    phn_no=models.IntegerField()
    passenger=models.IntegerField()
    book_date=models.DateTimeField()