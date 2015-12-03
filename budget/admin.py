from django.contrib import admin

from .models import Dochod, Wydatek, Waluta


class DochodAdmin(admin.ModelAdmin):
    list_display = ['użytkownik', 'kategoria', 'kwota', 'waluta', 'data_dodania']

class WydatekAdmin(admin.ModelAdmin):
    list_display = ['użytkownik', 'kategoria', 'kwota', 'waluta', 'data_dodania']

class WalutaAdmin(admin.ModelAdmin):
    list_display = ['waluta', 'przelicznik']

admin.site.register(Dochod, DochodAdmin)
admin.site.register(Wydatek, WydatekAdmin)
admin.site.register(Waluta, WalutaAdmin)