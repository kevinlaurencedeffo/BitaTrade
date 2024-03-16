from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('Dashboard',Dashboard, name="Dashboard"),
    path('Transaction',Transactions, name="Transaction"),
    path('payment/', payment, name='payment'),
    path('register/', register, name='register'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('resetPwd/', resetPwd, name='resetPwd'),
    
]