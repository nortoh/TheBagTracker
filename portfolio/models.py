from django.db import models
import datetime

class Coin(models.Model):
    ticker = models.CharField(max_length=5, default='NONE', verbose_name='Ticker', primary_key=True)

    def __str__(self):
        return "{}".format(self.ticker)

class Transaction(models.Model):
    # transaction_id = models.IntegerField(primary_key=True)
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    inserted_date = models.DateTimeField(auto_now_add=True)
    ticker = models.ForeignKey(Coin, to_field='ticker', on_delete=models.CASCADE)
    transaction_types = (('BUY', 'Buy'), ('SELL','Sell'))
    transaction_type = models.CharField(max_length=4, choices=transaction_types)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return "{}".format('I am a transaction weeeeeeeeeeeeeeeeee')

