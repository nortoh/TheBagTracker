from django import forms
from .models import Coin

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                # 'id': 'Username', 
                'type': 'useranme',
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

class TransactionAddForm(forms.Form):
    print(Coin.objects.all())

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
                'class': 'form-select',
                'id': 'floatingInput',
                'placeholder': 'Username'
            }
        )
    )

    transaction_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
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
