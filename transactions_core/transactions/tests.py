from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from rest_framework.authtoken.models import Token

from django.urls import reverse

from .serializers import TransactionCoreWalletSerializer, TransactionCoreWalletModelSerializer
from .models import TransactionCoreWallet, TransactionCoreTransactions
from django.conf import settings

class BaseViewTest(APITestCase):
    client = APIClient()
    uri = 'transaction_core_account'

    def setUp(self):
        #add some test data
        self.auth = 'X-Api-Key {}'.format(settings.API_KEY)

class TestCreateTransactionCoreCreateAccount(BaseViewTest):

    def test_create_district(self):
        params = {
            "account_number":"A002",
            "phone_number":"0780820744",
            "account_balance":0
        }
        response = self.client.post(reverse('transaction_core_account'), params)
        serialized = TransactionCoreWalletModelSerializer(params)
        self.assertEqual(serialized.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)