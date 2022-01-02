from django.shortcuts import render
from core.models import Crypto, CryptoPrice
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from .forms import CryptoForm


def index(request):
    # instantiate the form, with GET params (if they exist)
    form = CryptoForm(request.GET or None)

    # extract chosen ID (will default to first in queryset, as per form)
    crypto_id = form['name'].value()

    # get the cryptocurrency with the given ID
    choice = Crypto.objects.get(pk=crypto_id)
    
    # fetch price values for that cryptocurrency
    prices = CryptoPrice.objects.filter(crypto=choice).order_by('timestamp')

    # create Bokeh ColumnDataSource
    times = [c.timestamp for c in prices]
    values = [c.price for c in prices]
    cds = ColumnDataSource(data=dict(names=times, values=values))

    # create figure and draw line-chart
    fig = figure(height=500, title=f"{choice} prices")
    fig.line(source=cds, x='names', y='values', line_width=2)

    # generate script/div elements and include in context
    script, div = components(fig)
    context = {
        'script': script, 
        'div': div,
        'form': form,
    }

    # return fragment if HTMX request
    if request.htmx:
        return render(request, 'partials/chart.html', context)
    
    return render(request, 'index.html', context)