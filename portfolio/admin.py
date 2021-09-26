from django.contrib import admin
from .models import Coin, Transaction, Account, SupportTicket
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CoinAdmin(admin.ModelAdmin):
    list_display = ('ticker',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'transaction_date', 'base_pair', 'quote_pair', 'user_id', 'transaction_type', 'transaction_amount', 'transaction_fee', )
    list_filter = ('base_pair', 'quote_pair')
    search_fields = ('base_pair', 'quote_pair')
    ordering = ('id',)

class AccountAdmin(UserAdmin):
    list_display = (
        'id','username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active','date_of_birth'
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('is_student', 'is_teacher', 'mailing_address')
        })
    )
    # list_display = ('id', 'username')
    # list_filter = ('username',)
    # search_fields = ('username',)
    # ordering = ('id',)

class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'submission_date', 'subject', 'message' )
    list_filter = ('subject', 'message')
    search_fields = ('id', 'user_id', 'submission_date')
    ordering = ('id','submission_date')



admin.site.register(Coin, CoinAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(SupportTicket, SupportTicketAdmin)