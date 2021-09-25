from django.contrib import admin
from .models import Coin, Transaction, Account

# Register your models here.
class CoinAdmin(admin.ModelAdmin):
    list_display = ('ticker',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'inserted_date', 'base_pair', 'quote_pair', 'user_id', 'transaction_type', 'transaction_amount', 'transaction_fee', )
    list_filter = ('base_pair', 'quote_pair')
    search_fields = ('base_pair', 'quote_pair')
    ordering = ('id',)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username')
    list_filter = ('username',)
    search_fields = ('username',)
    ordering = ('user_id',)



admin.site.register(Coin, CoinAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Account, AccountAdmin)