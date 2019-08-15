from django.db import models

class TransactionCoreWallet(models.Model):
    wallet_number           = models.CharField(max_length=100, null=True, blank=True)
    wallet_contact          = models.CharField(max_length=255, null=True, blank=True)
    wallet_balance          = models.DecimalField(max_digits=20, decimal_places=3, default=0)  
    date_created            = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.wallet_number)

class TransactionCoreTransactions(models.Model):
    output_wallet           = models.ForeignKey(TransactionCoreWallet, on_delete=models.CASCADE, related_name='output_wallet')
    input_wallet            = models.ForeignKey(TransactionCoreWallet, on_delete=models.CASCADE, related_name='input_wallet')
    transaction_id          = models.CharField(max_length=255, blank=True, null=True)
    transaction_id_received = models.CharField(max_length=255, blank=True, null=True)
    transaction_amount      = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    transaction_status      = models.BooleanField(default=False)
    status_modified         = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    date_transacted         = models.DateTimeField(auto_now_add=True)