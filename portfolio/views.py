from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
import django_tables2 as tables

from .models import Transaction
from .forms import LoginForm
from datetime import datetime
from django.contrib.auth import authenticate, login, logout

class Index(View):
    template_name = 'index.html'

    def get(self, request):
        # bitcoin_trans = Transaction.objects.filter(ticker='BTC')

        if not request.user.is_authenticated:
            return HttpResponseRedirect('/login/') 

        return render(request, self.template_name, locals())

class LoginView(View):
    template_name = 'login/index.html'
    form_class = LoginForm

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

                return HttpResponseRedirect('/home/')
            else:
                print("Access denied!")

        return render(request, self.template_name, locals())

    def get(self, request):
        form = LoginForm()
        
        if request.user.is_authenticated:
            print('User is already logged in, redirecting to /home/')
            return HttpResponseRedirect('/home/')

        return render(request, self.template_name, locals())

class LogoutView(View):
    template_name = 'logout/index.html'

    def get(self, request):
        if request.user.is_authenticated:
            print('We have a user to logut')
            logout(request)
            return HttpResponseRedirect('/login/')
        else:
            print('No user is logged in, redirect to /login')
            return HttpResponseRedirect('/login/')
        
        return render(request, self.template_name, locals())

class HomeView(View):
    template_name = 'home/index.html'

    def get(self, request):
        return render(request, self.template_name, locals())

class TransactionsView(View):
    model = Transaction
    template_name = 'transactions.html'

    def get(self, request):
        
        if not request.user.is_authenticated:
            print('Someone is not logged in!')


        return render(request, self.template_name, locals())

class PortfolioView(View):
    template_name = 'portfolio/index.html'

    def get(self, request):
        # Data variables
        portfolio_data = Transaction.objects.filter(ticker='BTC')
        
        # Template variables
        portfolio = portfolio_data

        return render(request, self.template_name, locals())