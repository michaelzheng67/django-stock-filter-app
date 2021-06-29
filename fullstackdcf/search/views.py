from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import tickersymbol
from .forms import searchform
import yfinance as yf

# Create your views here.
class TickerSearch(CreateView):
    model = tickersymbol
    template_name = 'search/ticker_form.html'
    form_class = searchform


def Analysis(request):
    stock = tickersymbol.objects.last()
    yahoo_stock = yf.Ticker(stock.ticker)
    revenue = yahoo_stock.quarterly_earnings['Revenue']
    earnings = yahoo_stock.quarterly_earnings['Earnings']
    distribution = yahoo_stock.major_holders
    content = { 'ask' : yahoo_stock.info['ask'],
                'bid' : yahoo_stock.info['bid'],
                'spread' : round(yahoo_stock.info['ask'] - yahoo_stock.info['bid'],2),
                'name' : yahoo_stock.info['shortName'],
                'pegratio' : yahoo_stock.info['pegRatio'],
                'pricetobook' : round(yahoo_stock.info['priceToBook'],2),
                'trailingpe' : round(yahoo_stock.info['trailingPE'],2),
                'forwardpe' : round(yahoo_stock.info['forwardPE'],2),
                's1' : distribution[0][0],
                's2' : distribution[0][1],
                's3' : distribution[0][2],
                's4' : distribution[0][3],
                's5' : distribution[1][0],
                's6' : distribution[1][1],
                's7' : distribution[1][2],
                's8' : distribution[1][3],
                'revenue' : revenue[0] + revenue[1] + revenue[2] + revenue[3],
                'earnings' : earnings[0] + earnings[1] + earnings[2] + earnings[3]}
    return render(request, 'search/ticker_analysis.html', content)

# section for value (pegRatio, priceToBook, trailingPE, forwardPE) .info


