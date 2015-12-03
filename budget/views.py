from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django import forms

from .forms import SignUpForm, ContactForm, AddIncomeForm, AddExpensesForm
from .models import Dochod, Wydatek, Waluta


def home(request):
    title = "Welcome!!"
    #if request.user.is_authenticated():
    #    title = "My title " + str(request.user)
    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form,
    }

    if form.is_valid():

        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "No name specified"
        instance.full_name = full_name
        instance.save()


        context = {
        "title": "Thank you",
        }

    return render(request, "home.html", context)

def contact(request):
    title = 'Kontakt:'
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'Site contact form.'
        from_email = settings.EMAIL_HOST_USER
        to_email = from_email
        contact_message = "%s: %s via %s"%(form_full_name, form_message, form_email)
        send_mail(subject,
                  contact_message,
                  from_email,
                  [to_email],
                  fail_silently=True)
    context = {
        "form": form,
        "title": title,
    }

    return render(request, "forms.html", context)

def incomes(request):
    form = AddIncomeForm(request.POST or None, initial={'użytkownik': request.user})
    form.fields['użytkownik'].widget = forms.HiddenInput()

    title = 'Budżet: Dodaj dochód'
    suma = 0
    queryIncomes = Dochod.objects.all().filter(użytkownik__iexact=request.user).order_by('-data_dodania').filter(data_dodania__range=["2015-12-01", "2015-12-31"])
    for instance in Dochod.objects.all().filter(użytkownik__iexact=request.user).filter(data_dodania__range=["2015-12-01", "2015-12-31"]):
        if instance.waluta == "zł":
            suma += instance.kwota
        elif instance.waluta == "dolar":
            for waluta in Waluta.objects.all().filter(waluta__iexact="dolar"):
                suma += waluta.przelicznik * instance.kwota
        elif instance.waluta == "euro":
            for waluta in Waluta.objects.all().filter(waluta__iexact="euro"):
                suma += waluta.przelicznik * instance.kwota
        elif instance.waluta == "funt":
            for waluta in Waluta.objects.all().filter(waluta__iexact="funt"):
                suma += waluta.przelicznik * instance.kwota

    form.Meta.fields.insert(0, request.user)
    context = {
        'form': form,
        'title': title,
        'queryIncomes': queryIncomes,
        'suma': suma,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()


    return render(request, "incomes.html", context)

def expenses(request):
    form = AddExpensesForm(request.POST or None, initial={'użytkownik': request.user})
    form.fields['użytkownik'].widget = forms.HiddenInput()
    title = 'Budżet: Dodaj wydatek'
    suma = 0
    queryExpenses = Wydatek.objects.all().filter(użytkownik__iexact=request.user).order_by('-data_dodania').filter(data_dodania__range=["2015-12-01", "2015-12-31"])
    for instance in Wydatek.objects.all().filter(użytkownik__iexact=request.user).filter(data_dodania__range=["2015-12-01", "2015-12-31"]):
        if instance.waluta == "zł":
            suma += instance.kwota
        elif instance.waluta == "dolar":
            for waluta in Waluta.objects.all().filter(waluta__iexact="dolar"):
                suma += waluta.przelicznik * instance.kwota
        elif instance.waluta == "euro":
            for waluta in Waluta.objects.all().filter(waluta__iexact="euro"):
                suma += waluta.przelicznik * instance.kwota
        elif instance.waluta == "funt":
            for waluta in Waluta.objects.all().filter(waluta__iexact="funt"):
                suma += waluta.przelicznik * instance.kwota

    context = {
        'form': form,
        'title': title,
        'queryExpenses': queryExpenses,
        'suma': suma,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    return render(request, "expenses.html", context)

def budget(request):
    suma_dochodow = 0
    suma_wydatkow = 0
    for instance in Dochod.objects.all().filter(użytkownik__iexact=request.user).filter(data_dodania__range=["2015-12-01", "2015-12-31"]):
        if instance.waluta == "zł":
            suma_dochodow += instance.kwota
        elif instance.waluta == "dolar":
            for waluta in Waluta.objects.all().filter(waluta__iexact="dolar"):
                suma_dochodow += waluta.przelicznik * instance.kwota
        elif instance.waluta == "euro":
            for waluta in Waluta.objects.all().filter(waluta__iexact="euro"):
                suma_dochodow += waluta.przelicznik * instance.kwota
        elif instance.waluta == "funt":
            for waluta in Waluta.objects.all().filter(waluta__iexact="funt"):
                suma_dochodow += waluta.przelicznik * instance.kwota
    for instance in Wydatek.objects.all().filter(użytkownik__iexact=request.user).filter(data_dodania__range=["2015-12-01", "2015-12-31"]):
        if instance.waluta == "zł":
            suma_wydatkow += instance.kwota
        elif instance.waluta == "dolar":
            for waluta in Waluta.objects.all().filter(waluta__iexact="dolar"):
                suma_wydatkow += waluta.przelicznik * instance.kwota
        elif instance.waluta == "euro":
            for waluta in Waluta.objects.all().filter(waluta__iexact="euro"):
                suma_wydatkow += waluta.przelicznik * instance.kwota
        elif instance.waluta == "funt":
            for waluta in Waluta.objects.all().filter(waluta__iexact="funt"):
                suma_wydatkow += waluta.przelicznik * instance.kwota

    saldo = suma_dochodow - suma_wydatkow

    context = {
        'suma_dochodow': suma_dochodow,
        'suma_wydatkow': suma_wydatkow,
        'saldo': saldo,
    }

    return render(request, "budget.html", context)

def savings(request):
    return render(request, "savings.html", {})
