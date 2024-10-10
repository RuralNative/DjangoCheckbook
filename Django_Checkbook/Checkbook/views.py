from django.shortcuts import render, redirect
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction

# Create your views here.

def home(request):
    return render(request, 'Checkbook/index.html')

def balance_sheet(request):
    return render(request, 'Checkbook/BalanceSheet.html')

def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_accounts')
    else:
        form = AccountForm()
    return render(request, 'Checkbook/CreateNewAccount.html', {'form': form})

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_transactions')
    else:
        form = TransactionForm()
    return render(request, 'Checkbook/AddTransaction.html', {'form': form})

