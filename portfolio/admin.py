from django.contrib import admin
from .models import Coin, Transaction

# Register your models here.
class CoinAdmin(admin.ModelAdmin):
    list_display = ('ticker',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'inserted_date', 'ticker', 'transaction_type', 'transaction_amount', 'transaction_fee', )
    list_filter = ('ticker',)

admin.site.register(Coin, CoinAdmin)
admin.site.register(Transaction, TransactionAdmin)
