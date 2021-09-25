from django import forms


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