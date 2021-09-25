import django_tables2 as tables
from .models import Transaction

class TransactionsTable(tables.Table):
    class Meta:
        model = Transaction
        template_name = "django_tables2/bootstrap4.html"
        fields = ('date', 'base_pair', 'quote_pair', 'inserted_date', 'transaction_type', 'transaction_amount', 'transaction_fee')


class PortfolioTable(tables.Table):
    class Meta:
        model = Transaction
        template_name = 'django_tables2/bootstrap4.html'