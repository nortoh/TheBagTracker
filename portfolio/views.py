from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
import django_tables2 as tables

from .models import Transaction
from .forms import SignInForm
from datetime import datetime
from django.contrib.auth import authenticate, login

class Index(View):
    template_name = 'index.html'

    def get(self, request):
        # bitcoin_trans = Transaction.objects.filter(ticker='BTC')
        return render(request, self.template_name, locals())

class SignInView(View):
    template_name = 'sign_in.html'
    form_class = SignInForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            print(f'Logging in as {username}')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                print("We logged in!")
            else:
                print("Access denied!")

        return render(request, self.template_name, locals())

    def get(self, request):
        form = SignInForm()
        return render(request, self.template_name, locals())

class TransactionsView(View):
    model = Transaction
    template_name = 'transactions.html'

class PortfolioView(View):
    template_name = 'portfolio/index.html'

    def get(self, request):
        # Data variables
        portfolio_data = Transaction.objects.filter(ticker='BTC')
        
        # Template variables
        portfolio = portfolio_data

        return render(request, self.template_name, locals())