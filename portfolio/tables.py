import django_tables2 as tables
from .models import Transaction

class CustomTemplateColumn(tables.TemplateColumn):
    def render(self, record, table, value, bound_column, **kwargs):
         return super(CustomTemplateColumn, self).render(record, table, value, bound_column, **kwargs)

class TransactionsTable(tables.Table):
    remove = CustomTemplateColumn('<button type="button" class="btn btn-danger" delete-link="">Remove</button>')
    class Meta:
        model = Transaction
        template_name = "django_tables2/bootstrap4.html"
        fields = ('date', 'base_pair', 'quote_pair', 'transaction_date', 'transaction_type', 'transaction_amount', 'transaction_fee', 'remove')

class PortfolioTable(tables.Table):
    class Meta:
        model = Transaction
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('ticker', 'price')
