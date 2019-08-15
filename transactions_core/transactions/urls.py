from django.urls import path, include
from .views import TransactionCoreWalletView

urlpatterns = [
    path('transaction_core_account/', TransactionCoreWalletView.as_view(), name="transaction_core_account"),
]