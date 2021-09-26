import django_tables2 as tables
from .models import Transaction
from django.utils.html import format_html
class CustomTemplateColumn(tables.TemplateColumn):
    def render(self, record, table, value, bound_column, **kwargs):
         return super(CustomTemplateColumn, self).render(record, table, value, bound_column, **kwargs)

class TransactionsTable(tables.Table):
    remove = CustomTemplateColumn('<button type="button" class="btn btn-danger" delete-link="">Remove</button>')

    def render_base_pair(self, value):
        return format_html("<b><img width='15' height='15' src='/static/img/coins/{}.png' />&nbsp;{}</b>", value, value)

    def render_quote_pair(self, value):
        return format_html("<b><img width='15' height='15' src='/static/img/coins/{}.png' />&nbsp;{}</b>", value, value)

    class Meta:
        model = Transaction
        template_name = "django_tables2/bootstrap4.html"
        fields = ('date', 'base_pair', 'quote_pair', 'transaction_date', 'transaction_type', 'transaction_amount', 'transaction_fee', 'remove')

class PortfolioTable(tables.Table):
    class Meta:
        model = Transaction
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('ticker', 'price')
