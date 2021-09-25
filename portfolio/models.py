from django.db import models
import datetime

class Coin(models.Model):
    ticker = models.CharField(max_length=5, default='NONE', verbose_name='Ticker', primary_key=True)
    def __str__(self):
        return "{}".format(self.ticker)

class Account(models.Model):
    username = models.CharField(max_length=30)
    user_id = models.IntegerField(primary_key=True)

class Wallet(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name="Wallet")

class Transaction(models.Model):
    # transaction_id = models.IntegerField(primary_key=True)
    id = models.IntegerField(primary_key=True, verbose_name='ID')
    date = models.DateTimeField(verbose_name='Date')
    inserted_date = models.DateTimeField(auto_now_add=True, verbose_name='Date Added')
    base_pair = models.ForeignKey(Coin, to_field='ticker', on_delete=models.CASCADE, related_name='base_coin_pair')
    quote_pair = models.ForeignKey(Coin, to_field='ticker', on_delete=models.CASCADE, related_name='quote_coin_pair')
    user_id = models.ForeignKey(Account, to_field='user_id', on_delete=models.CASCADE)
    transaction_types = (('BUY', 'Buy'), ('SELL','Sell'))
    transaction_type = models.CharField(max_length=4, choices=transaction_types)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return "Something soon"

