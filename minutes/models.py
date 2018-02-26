from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)


class Person(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class Meeting(models.Model):
    attendees = models.ManyToManyField(Person)
    title = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()