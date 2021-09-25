from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from .models import Transaction, Coin
from datetime import datetime

class Index(View):
    template_name = 'index.html'

    def get(self, request):

        # bitcoin = Coin(ticker='BTC')
        # bitcoin.save()        
        
        bitcoin = Coin.objects.get(ticker='BTC')

        new_transaction = Transaction(
            date=datetime.now(),
            ticker=bitcoin,
            transaction_type='BUY',
            transaction_amount=10200,
            transaction_fee=10.99)
        new_transaction.save()

        return render(request, self.template_name, locals())