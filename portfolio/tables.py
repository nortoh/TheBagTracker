import django_tables2 as tables
from .models import Transaction
from django.utils.html import format_html
class CustomTemplateColumn(tables.TemplateColumn):
    def render(self, record, table, value, bound_column, **kwargs):
         return super(CustomTemplateColumn, self).render(record, table, value, bound_column, **kwargs)

class TransactionsTable(tables.Table):
    remove = CustomTemplateColumn('<button type="button" class="btn btn-danger" delete-link="">Remove</button>', verbose_name="")

    def render_base_pair(self, value):
        return format_html("<b><img width='15' height='15' src='/static/img/coins/{}.png' />&nbsp;{}</b>", value, value)

    def render_quote_pair(self, value):
        return format_html("<b><img width='15' height='15' src='/static/img/coins/{}.png' />&nbsp;{}</b>", value, value)

    def render_transaction_amount(self, value):
        return format_html("<b>${}</b>", value)

    def render_transaction_fee(self, value):
        return format_html("<b>${}</b>", value)

    class Meta:
        model = Transaction
        template_name = "django_tables2/bootstrap4.html"
        fields = ('date', 'base_pair', 'quote_pair', 'transaction_date', 'transaction_type', 'transaction_amount', 'transaction_fee', 'remove')

class PortfolioTable(tables.Table):

    def render_ticker(self, value):
        return format_html("<b><img width='15' height='15' src='/static/img/coins/{}.png' />&nbsp;{}</b>", value, value)

    def render_price(self, value):
        return format_html("<b>${}</b>", value)

    price = tables.Column(verbose_name="Value", attrs={'td': {'class': lambda value: 'text-green' if float(value.strip('$</b>')) >= 0 else 'text-red'}})

    class Meta:
        model = Transaction
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('ticker', 'price')
