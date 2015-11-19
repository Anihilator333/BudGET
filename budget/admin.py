from django.contrib import admin

from .forms import SignUpForm, AddCategoryForm
from .models import Dochod, Wydatek

class DochodAdmin(admin.ModelAdmin):
    list_display = ['użytkownik', 'kategoria', 'kwota', 'data_dodania']

class WydatekAdmin(admin.ModelAdmin):
    list_display = ['użytkownik', 'kategoria', 'kwota', 'data_dodania']

admin.site.register(Dochod, DochodAdmin)
admin.site.register(Wydatek, WydatekAdmin)