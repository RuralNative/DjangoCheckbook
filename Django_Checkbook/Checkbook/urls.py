from django.urls import path
from .views import home, balance_sheet, create_account, add_transaction

urlpatterns = [
    path('', home, name='home'),
    path('balance_sheet', balance_sheet, name='balance_sheet'),
    path('create/', create_account, name='create_account'),
    path('add_transaction/', add_transaction, name='add_transaction'),
]