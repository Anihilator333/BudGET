from django.db import models
from django.shortcuts import render

class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=150, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    udpated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email

class Categories(models.Model):
    user = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=50, blank=False)

class Dochod(models.Model):
    użytkownik = models.CharField(max_length=50, blank=False)
    kategoria = models.CharField(max_length=50, blank=False)
    kwota = models.IntegerField(blank=False, default=0)
    data_dodania = models.DateTimeField(auto_now_add=True, auto_now=False)

class Wydatek(models.Model):
    użytkownik = models.CharField(max_length=50, blank=False)
    kategoria = models.CharField(max_length=50, blank=False)
    kwota = models.IntegerField(blank=False, default=0)
    data_dodania = models.DateTimeField(auto_now_add=True, auto_now=False)