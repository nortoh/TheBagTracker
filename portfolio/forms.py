from django import forms
from .models import Coin, Account
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib import messages

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'username',
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control',
                'id': 'floatingPassword',
                'placeholder': 'Password'
            }
        )
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'username',
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': 'Username'
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control',
                'id': 'floatingPassword',
                'placeholder': 'Password'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control',
                'id': 'floatingPassword',
                'placeholder': 'Password'
            }
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': 'John'
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': 'Doe'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'type': 'email',
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': 'example@example.com'
            }
        )
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(
            format=('%d-%m-%Y'),
            attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': 'Select a date'
            }
        )
    )

    # class Meta:
    #     model = Account
    #     fields = ("username", "first_name", "last_name", "password1", "password2", "birth_date", "email")

    # def clean_password2(self):
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']
    #
    #     if password1 and password2 and password1 != password2:
    #         #messages.error(self, 'Passwords don\'t match')
    #         raise ValidationError("Password don't match")
    #     return password2

    def clean(self):

        # data from the form is fetched using super function
        super(RegisterForm, self).clean()

        # extract the username and text field from the data
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        # conditions to be met for form

        result = False

        for x in password1:
            if x.isupper():
                result= True
                break
        if len(username) < 5 or len(username) > 16:
            self._errors['username'] = self.error_class([
                'Username needs to be between 6 and 16 characters'])
        if len(password1) < 5 or len(password1) > 16:
            self._errors['password1'] = self.error_class([
                'Password needs to be between 6 and 16 characters'])
        if (password1 != password2):
            self._errors['password2'] = self.error_class([
                'Password don\'t match'])
        if (result == False):
            self._errors['password1'] = self.error_class([
                'Password needs to have an upper case'])


        # return any errors if found
        return self.cleaned_data





# class RegisterForm(UserCreationForm):
#     #username = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
#     #first_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name')
#     #last_name=forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, help_text='Last name')
#     #email=forms.EmailField(forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Enter a valid email address')
#     #password1=forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
#     #password2=forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))
#     birth_date = forms.CharField(
#             widget=forms.DateInput(
#                 format=('%d-%m-%Y'),
#                 attrs={
#                     'type': 'birth_date',
#                     'class': 'form-control',
#                     'id': 'floatingInput',
#                     'placeholder': 'Select a date'
#                 }
#             )
#         )
#
#     class Meta(UserCreationForm.Meta):
#         model = Account
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class TransactionAddForm(forms.Form):
    base_pair = forms.ChoiceField(
        choices=[(o.ticker, str(o)) for o in Coin.objects.all()],
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'floatingInput',
                'placeholder': 'Username'
            }
        )
    )

    quote_pair = forms.ChoiceField(
        choices=[(o.ticker, str(o)) for o in Coin.objects.all()],
        widget=forms.Select(
            attrs={
                'type': 'list',
                'class': 'form-select',
                'id': 'floatingInput',
                'placeholder': 'Username'
            }
        )
    )

    transaction_date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': '12/25/1996'
            }
        )
    )

    transaction_amount = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': '$9000'
            }
        )
    )

    transaction_fee = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': '$9000'
            }
        )
    )

    transaction_type = forms.ChoiceField(
        choices=[('BUY', 'Buy'), ('SELL', 'Sell')],
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'floatingInput',
                'placeholder': 'Username'
            }
        )
    )

class SupportTicketForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': 'Subject'
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': 'Whats wrong?'
            }
        )
    )
