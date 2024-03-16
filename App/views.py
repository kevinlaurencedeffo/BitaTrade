from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from .models import CompteUser,Transaction,OrdreMarche,Crypto,Historique
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import mplfinance as mpl
import datetime as dt
import requests
import ccxt
import pandas as pd

def register(request):
    message = {
       
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            cmp1 =CompteUser.objects.create(iduser=user.pk,tel=telephone,solde=0,devise="BTC",libele='Compte BTC')
            cmp2 =CompteUser.objects.create(iduser=user.pk,tel=telephone,solde=0,devise="ETH",libele='Compte ETH')
            cmp3 =CompteUser.objects.create(iduser=user.pk,tel=telephone,solde=0,devise="USD",libele='Compte USD')
            message['msg'] = "Compte creer avec success Dans quelques instants un agent BITA Trade va vous appeller pour vous guider dans la finalisation et activation de votre compte. Restez donc connecter car le prochain appel sera probablement nous. Pour le moment veuillez vous connecter" 
            message['icon'] = 'success'
        except Exception as e:
            message['msg'] = "Remplissez correctement les champs!"
            message['icon'] = 'error'
    return render(request, 'auth/register.html',{'message':message})

def Login(request):
    user = ''
    message = {
    }
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            message['msg'] = "Bienvenu"
            message['icon'] = 'success'
            return redirect('Dashboard') 
        else:
            message['msg'] = "Nom utilisateur ou mot de passe Incorrect"
            message['icon'] = 'error'

    return render(request, 'auth/login.html',{'user':user,'message': message})

@login_required
def Logout(request):
    logout(request)
    return redirect('login')

def resetPwd(request):
    return render(request,'auth/forgetpwd.html')


def index(request):
    binance = ccxt.binance()
    markets = binance.load_markets()
    btc = binance.fetch_ticker('BTC/USD')
    eth = binance.fetch_ticker('ETH/USD')
    xrp = binance.fetch_ticker('XRP/USD')
    bnb = binance.fetch_ticker('BNB/USD')
    sol = binance.fetch_ticker('SOL/USD')
    car = binance.fetch_ticker('ADA/USD')
    ava = binance.fetch_ticker('AVAX/USD')
    crp = {
        'btc': {
            'open': btc['close'],
            'percentage': btc['percentage']
        },
        'eth': {
            'open': eth['close'],
            'percentage': eth['percentage']
        },
        'xrp': {
            'open': xrp['close'],
            'percentage': xrp['percentage']
        },
        'bnb': {
            'open': bnb['close'],
            'percentage': bnb['percentage']
        },
        'sol': {
            'open': sol['close'],
            'percentage': sol['percentage']
        },
        'car': {
            'open': car['close'],
            'percentage': car['percentage']
        },
        'ava': {
            'open': ava['close'],
            'percentage': ava['percentage']
        }
    }
    
    
   
    return render(request,'base.html',{'crp':crp})

@login_required
def Dashboard(request):
    today = dt.date.today()
    hier = dt.date.min
    heure1 = dt.time.min
    heure2 = dt.time.max
    user = request.user
    cmp = CompteUser.objects.filter(iduser=request.user.pk).values()
    btc=cmp[0]
    eth=cmp[1]
    usdt=cmp[2]
    print(cmp)
    return render(request,"Dashboard.html",{'today':today,'hier':hier,'heure1':heure1,'heure2':heure2,'btc':btc,'user':user,'eth':eth,'usdt':usdt})

#######Les classes based view########
def payment(request):
    message=''
    if request.method=='POST':  
        message = "Votre Paiement est Encour de traitement vous allez recevoir une notification dans quelques instant"
    return render(request,'payment.html',{'message': message})

@login_required
def Transactions(request):
    today = dt.date.today()
    hier = dt.date.min
    heure1 = dt.time.min
    heure2 = dt.time.max
    user = request.user
    cmp = CompteUser.objects.filter(iduser=request.user.pk).values()
    btc=cmp[0]
    eth=cmp[1]
    usdt=cmp[2]
    print(cmp)
    return render(request,"transact.html",{'today':today,'hier':hier,'heure1':heure1,'heure2':heure2,'btc':btc,'user':user,'eth':eth,'usdt':usdt})

##Compte
class CompteListView(ListView):
    model = CompteUser
    template_name = ".html"

class CompteCreateView(CreateView):
    model = CompteUser
    template_name = ".html"

class CompteDeleteView(DeleteView):
    model = CompteUser
    template_name = ".html"

class CompteUpdateView(UpdateView):
    model = CompteUser
    template_name = ".html"

##Crypto
class CryptoListView(ListView):
    model = Crypto
    template_name = ".html"

class CryptoCreateView(CreateView):
    model = Crypto
    template_name = ".html"

class CryptoUpdateView(UpdateView):
    model = Crypto
    template_name = ".html"

class CryptoDeleteView(DeleteView):
    model = Crypto
    template_name = ".html"

##Transaction
class TransactionListView(ListView):
    model = Transaction
    template_name = "transact.html"

class TransactionCreateView(CreateView):
    model = Transaction
    template_name = "transact.html"

class TransactionUpdateView(UpdateView):
    model = Transaction
    template_name = ".html"

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = ".html"

##Historique
class HistoriqueListView(ListView):
    model = Historique
    template_name = ".html"

class HistoriqueCreateView(CreateView):
    model = Historique
    template_name = ".html"

class HistoriqueUpdateView(UpdateView):
    model = Historique
    template_name = ".html"

class HistoriqueDeleteView(DeleteView):
    model = Historique
    template_name = ".html"

##Ordre de Marche
class OrdreMarcheListView(ListView):
    model = OrdreMarche
    template_name = ".html"

class OrdreMarcheCreateView(CreateView):
    model = OrdreMarche
    template_name = ".html"

class OrdreMarcheUpdateView(UpdateView):
    model = OrdreMarche
    template_name = ".html"

class OrdreMarcheDeleteView(DeleteView):
    model = OrdreMarche
    template_name = ".html"
