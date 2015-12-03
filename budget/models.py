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

class Waluta(models.Model):
    waluta = models.CharField(max_length=10, blank=False)
    przelicznik = models.DecimalField(blank=False, max_digits=10, decimal_places=4)

class Dochod(models.Model):
    użytkownik = models.CharField(max_length=50, blank=False)
    kategoria = models.CharField(max_length=50, blank=False)
    kwota = models.DecimalField(blank=False, default=0, max_digits=6, decimal_places=2)
    waluta = models.CharField(max_length=10, blank=False, default="zł")
    data_dodania = models.DateTimeField(auto_now_add=True, auto_now=False)

class Wydatek(models.Model):
    użytkownik = models.CharField(max_length=50, blank=False)
    kategoria = models.CharField(max_length=50, blank=False)
    kwota = models.DecimalField(blank=False, default=0, max_digits=6, decimal_places=2)
    waluta = models.CharField(max_length=10, blank=False, default="zł")
    data_dodania = models.DateTimeField(auto_now_add=True, auto_now=False)