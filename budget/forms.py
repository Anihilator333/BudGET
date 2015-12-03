from django import forms

from .models import SignUp, Categories, Dochod, Wydatek


class ContactForm(forms.Form):

    nazwa = forms.CharField(required=False)
    twoj_email = forms.EmailField(required=True)
    wiadomość = forms.CharField()


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email', 'full_name']

    def clean_email(self):
        """
        method to validate if email is correct(and it fits our requirements)
        :return: valid email if it pass all validation
        """
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        # domain, extension = provider.split(".")
        if "edu" not in provider:
            raise forms.ValidationError("Please use a valid .edu email address.")
        return email

    def clean_full_name(self):
        """
        similar to clean_email method but it validates name
        :return:
        """
        full_name = self.cleaned_data.get('full_name')
        return full_name


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['user', 'name']

    def clean_user(self):
        user = self.cleaned_data.get('user')
        if not user:
            raise forms.ValidationError('To pole jest wymagane.')
        for i in '`~!@#$%^&*()_+|-=\{}[]:";\'<>?,./':
            if i in user:
                raise forms.ValidationError('To pole nie może mieć znaków specjalnych.')

        return user

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for i in '`~!@#$%^&*()_+|-=\{}[]:";\'<>?,./':
            if i in name:
                raise forms.ValidationError('To pole nie może mieć znaków specjalnych.')

        return name


class AddIncomeForm(forms.ModelForm):
    class Meta:
        model = Dochod
        fields = ['użytkownik', 'kategoria', 'kwota', 'waluta']

    def clean_użytkownik(self):
        użytkownik = self.cleaned_data.get('użytkownik')

        for i in '`~!@#$%^&*()_+|-=\{}[]:";\'<>?,./':
            if i in użytkownik:
                raise forms.ValidationError('To pole nie może mieć znaków specjalnych.')

        return użytkownik

    def clean_kategoria(self):
        kategoria = self.cleaned_data.get('kategoria')
        for i in '`~!@#$%^&*()_+|-=\{}[]:";\'<>?,./':
            if i in kategoria:
                raise forms.ValidationError('To pole nie może mieć znaków specjalnych.')

        return kategoria

    def clean_kwota(self):
        kwota = self.cleaned_data.get('kwota')
        if kwota <= 0:
            raise forms.ValidationError('Podana kwota nie może być mniejsza lub równa 0.')

        return kwota

    def clean_waluta(self):
        waluta = self.cleaned_data.get('waluta')
        lista_walut = ['dolar', 'euro', 'funt', 'zł']
        if waluta not in lista_walut:
            raise forms.ValidationError('Podana waluta nie jest dostępna(wybierz dolar, euro, funt lub zł).')

        return waluta


class AddExpensesForm(forms.ModelForm):
    class Meta:
        model = Wydatek
        fields = ['użytkownik', 'kategoria', 'kwota', 'waluta']

    def clean_użytkownik(self):
        użytkownik = self.cleaned_data.get('użytkownik')

        for i in '`~!@#$%^&*()_+|-=\{}[]:";\'<>?,./':
            if i in użytkownik:
                raise forms.ValidationError('To pole nie może mieć znaków specjalnych.')

        return użytkownik

    def clean_kategoria(self):
        kategoria = self.cleaned_data.get('kategoria')
        for i in '`~!@#$%^&*()_+|-=\{}[]:";\'<>?,./':
            if i in kategoria:
                raise forms.ValidationError('To pole nie może mieć znaków specjalnych.')

        return kategoria

    def clean_kwota(self):
        kwota = self.cleaned_data.get('kwota')
        if kwota <= 0:
            raise forms.ValidationError('Podana kwota nie może być mniejsza lub równa 0.')

        return kwota

    def clean_waluta(self):
        waluta = self.cleaned_data.get('waluta')
        lista_walut = ['dolar', 'euro', 'funt', 'zł']
        if waluta not in lista_walut:
            raise forms.ValidationError('Podana waluta nie jest dostępna(wybierz dolar, euro, funt lub zł).')

        return waluta
