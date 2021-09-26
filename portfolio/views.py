from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
import django_tables2 as tables
from django_tables2 import SingleTableView
from websocket import create_connection, WebSocket

from django.core.exceptions import ValidationError

import socket
import json

from .models import Transaction, Account, Coin, SupportTicket
from .forms import LoginForm, TransactionAddForm,RegisterForm, SupportTicketForm
from .tables import TransactionsTable, PortfolioTable
from datetime import datetime
from django.contrib.auth import authenticate, login, logout

class LoginView(View):
    template_name = 'login/index.html'
    form_class = LoginForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            print(f'Logging in as {username}')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                print("We logged in!")

                # Create the account object if we do not have
                Account.objects.get_or_create(
                    id=user.id,
                    username=username
                )
                
                return HttpResponseRedirect('/')
            else:
                print("Access denied!")

        return render(request, self.template_name, locals())

    def get(self, request):
        form = LoginForm()
        
        if request.user.is_authenticated:
            print('User is already logged in, redirecting to /')
            return HttpResponseRedirect('/')

        return render(request, self.template_name, locals())

class LogoutView(View):
    template_name = 'logout/index.html'

    def get(self, request):
        if request.user.is_authenticated:
            print('We have a user to logout')
            logout(request)
            return HttpResponseRedirect('/signin/')
        else:
            print('No user is logged in, redirect to /signin')
            return HttpResponseRedirect('/signin/')
        
        return render(request, self.template_name, locals())

class Portfolio(object):

    """
    <id, BTC, USD, 100, 7/10/21>

    Let's convert everything to dollars for now, so if we have a trading pair such as
    BTC/USD Buy, we will add the price of 1 BTC * transaction_amount to the dict entry
    for BTC.

    If we have a trading pair such as BTC/ETH, we first need to do price of 1 ETH, then multiple

    """
    def __init__(self):
        self.transactions = []

    def fill(self, transactions):
        self.total_amount = dict()
        self.transactions = transactions
        self.breakdown()

    def breakdown(self):
        for transaction in self.transactions:
            base_pair = transaction.base_pair
            base_pair_ticker = base_pair.ticker
            transaction_type = transaction.transaction_type
            transaction_amount = transaction.transaction_amount
            transaction_fee = transaction.transaction_fee

            if not base_pair_ticker in self.total_amount.keys():
                api_price = 1
                price = (transaction_amount * api_price) - transaction_fee
                self.total_amount[base_pair.ticker] = price
            else:
                if transaction_type == 'BUY':
                    api_price = 1
                    price = (transaction_amount * api_price) - transaction_fee
                    self.total_amount[base_pair_ticker] = self.total_amount[base_pair_ticker] + price
                    print(f'We are adding {price}')
                elif transaction_type == 'SELL':
                    api_price = 1
                    price = (transaction_amount * api_price) - transaction_fee
                    self.total_amount[base_pair_ticker] = self.total_amount[base_pair_ticker] - transaction_amount

        results = []
        for ticker, price in self.total_amount.items():
            results.append({
                'ticker': ticker,
                'price': price
            })

        self.table_data = results

class HomeView(View):
    model = Transaction
    table_class = PortfolioTable
    template_name = 'home/index.html'
    portfolio = Portfolio()


    # Get coin stats before passing to API
    def construct_coin_stats(self, request):
        all_transactions = Transaction.objects.filter(user_id=request.user.id)
        print(f'all_transactions: {all_transactions}')
        # For now, build the portfolio on every GET
        self.portfolio.fill(all_transactions)

    def get(self, request):
        if not request.user.is_authenticated:
            print('Someone is not logged in!')
            print('No user is logged in, redirect to /signin')
            return HttpResponseRedirect('/signin/')
        
        nbar = 'home'

        account = Account.objects.get(
            id=request.user.id
        )

        user_transactions = Transaction.objects.filter(user_id=account.id)
        self.portfolio.fill(user_transactions)
        portfolio_table = PortfolioTable(self.portfolio.table_data)
        return render(request, self.template_name, locals())


class RegisterView(View):
    template_name = 'register.html'
    form_class = RegisterForm

    def post(self, request):
        form = self.form_class(request.POST)

        print(str(request.POST))
        print(str(form.is_valid()))


        if form.is_valid():
            print("Valid!!!")
            username = request.POST['username']
            password = request.POST['password1']
            confirm_password = request.POST['password2']
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            birth_date = request.POST['birth_date']
            test = Account.objects.create_user(
                username=username,
                password=password,
                email=email,
                date_of_birth=birth_date,
                first_name=first_name,
                last_name=last_name
            )
            print(str(test))

        else:
            print("Not valid!")
            messages = form.errors
            print(messages)
            #return render(request, "register.html", {"messages": form.errors})


        return render(request, self.template_name, locals())

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, locals())



class TransactionsView(SingleTableView):
    model = Transaction
    table_class = TransactionsTable
    template_name = 'transactions/index.html'

    def get(self, request):
        if not request.user.is_authenticated:
            print('Someone is not logged in!')
            print('No user is logged in, redirect to /signin')
            return HttpResponseRedirect('/signin/')
        
        nbar = 'transactions'

        account = Account.objects.get(
            id=request.user.id
        )
        
        # Pull and make contents
        user_transactions = Transaction.objects.filter(user_id=account.id)
        transaction_table = TransactionsTable(user_transactions)
        transaction_table.order_by ='-Date'

        return render(request, self.template_name, locals())

class TransactionView(View):
    template_name = 'transaction/view.html'

    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'

    def get(self, request):
        return render(request, self.template_name, locals())

class TransactionAddView(View):
    template_name = 'transactions/add.html'
    form_class = TransactionAddForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            account = Account.objects.get(
                id=request.user.id
            )

            base_pair = request.POST['base_pair']
            quote_pair = request.POST['quote_pair']
            date = datetime.now()
            transaction_date = request.POST['transaction_date']
            transaction_amount = request.POST['transaction_amount']
            transaction_type = request.POST['transaction_type']
            transaction_fee = request.POST['transaction_fee']

            new_transaction = Transaction(
                date=date,
                base_pair = Coin.objects.get(ticker=base_pair),
                quote_pair = Coin.objects.get(ticker=quote_pair),
                user_id = account,
                transaction_date=transaction_date,
                transaction_type = transaction_type,
                transaction_amount = transaction_amount,
                transaction_fee = transaction_fee
            )

            new_transaction.save()
            return HttpResponseRedirect('/transactions/')
        return render(request, self.template_name, locals())

    def get(self, request):
        form = TransactionAddForm()

        if not request.user.is_authenticated:
            print('User is already logged in, redirecting to /')
            return HttpResponseRedirect('/')

        return render(request, self.template_name, locals())

class PortfolioView(View):
    template_name = 'portfolio/index.html'

    def get(self, request):
        nbar = 'Portfolio'

        portfolio_data = Transaction.objects.filter(ticker='BTC')
        
        # Template variables
        portfolio = portfolio_data

        return render(request, self.template_name, locals())


class SupportTicketView(View):
    template_name = 'support.html'
    form_class = SupportTicketForm

    def post(self, request):
        form = self.form_class(request.POST)


        if form.is_valid():
            subject = request.POST['subject']
            message = request.POST['message']
            current_user_id = request.user.id
            current_user = Account.objects.get(id=current_user_id)
            print("This is the current user: " + str(current_user))
            SupportTicket.objects.create(
                subject=subject,
                message=message,
                user_id=current_user,
            )

        return render(request, self.template_name, locals())

    def get(self, request):
        form = SupportTicketForm()
        return render(request, self.template_name, locals())