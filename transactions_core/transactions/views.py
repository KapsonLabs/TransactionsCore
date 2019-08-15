from rest_framework import generics
from django.http import QueryDict
import datetime

from django.http import Http404
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework import permissions

# from accounts.permissions import ClientPermissions, MerchantPermissions, MerchantCientPermissions
# from wallets.models import Wallet, WalletTransactions
# from wallets.serializers import WalletDetailsSeriliazer, WalletTransactionsSerializer, WalletTransactionsDetailSerializer

from .models import TransactionCoreWallet
from .serializers import TransactionCoreWalletSerializer, TransactionCoreWalletModelSerializer

# from wallets.helpers import generate_transaction_id
# from accounts.permissions import HasServiceAPIKey

class TransactionCoreWalletView(APIView):

    def post(self, request):
        transactionwalletcreate = TransactionCoreWalletSerializer(data=request.data)
        if transactionwalletcreate.is_valid():
            try:
                transactionwallet = {
                    "wallet_number":transactionwalletcreate.data['account_number'],
                    "wallet_contact":transactionwalletcreate.data['phone_number'],
                    "wallet_balance":transactionwalletcreate.data['account_balance'],
                }

                transaction_core_wallet = TransactionCoreWalletModelSerializer(data=transactionwallet)
                transaction_core_wallet.is_valid(raise_exception=True)
                transaction_core_wallet.save()

                data_dict = {"status":201, "wallet_details":transaction_core_wallet.data,}
                return Response(data_dict, status=status.HTTP_201_CREATED)

            except:
                data_dict = {"status":404, "error":"Invalid number, Please dont create ur own accounts"}
                return Response(data_dict, status=status.HTTP_404_NOT_FOUND)
        return Response(transaction_core_wallet.errors, status=status.HTTP_400_BAD_REQUEST)
        

class TransactionCoreWalletView(APIView):

    def post(self, request):
        transactionwalletcreate = TransactionCoreWalletSerializer(data=request.data)
        if transactionwalletcreate.is_valid():
            try:
                transactionwallet = {
                    "wallet_number":transactionwalletcreate.data['account_number'],
                    "wallet_contact":transactionwalletcreate.data['phone_number'],
                    "wallet_balance":transactionwalletcreate.data['account_balance'],
                }

                transaction_core_wallet = TransactionCoreWalletModelSerializer(data=transactionwallet)
                transaction_core_wallet.is_valid(raise_exception=True)
                transaction_core_wallet.save()

                data_dict = {"status":201, "wallet_details":transaction_core_wallet.data,}
                return Response(data_dict, status=status.HTTP_201_CREATED)

            except:
                data_dict = {"status":404, "error":"Invalid number, Please dont create ur own accounts"}
                return Response(data_dict, status=status.HTTP_404_NOT_FOUND)
        return Response(transaction_core_wallet.errors, status=status.HTTP_400_BAD_REQUEST)

