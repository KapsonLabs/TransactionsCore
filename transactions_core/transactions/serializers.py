from rest_framework import serializers
from .models import TransactionCoreWallet

class TransactionCoreWalletSerializer(serializers.Serializer):
    """
    A core wallet serializer data receiver
    """
    account_number     = serializers.CharField(max_length=250)
    phone_number       = serializers.CharField(max_length=250)
    account_balance    = serializers.DecimalField(max_digits=20, decimal_places=3)

class TransactionCoreWalletModelSerializer(serializers.ModelSerializer):
    """
    A core wallet serializer
    """

    class Meta:
        model = TransactionCoreWallet
        fields = ('id','wallet_number','wallet_contact', 'wallet_balance', 'date_created')

class TransactionCoreTransactionsSerializer(serializers.Serializer):
    """
    A core wallet transaction serializer data receiver
    """
    account_number     = serializers.CharField(max_length=250)
    phone_number       = serializers.CharField(max_length=250)
    account_balance    = serializers.DecimalField(max_digits=20, decimal_places=3)