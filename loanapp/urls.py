from django.urls import path
from .views import LoanCalculatorView

urlpatterns = [
    path('loan-repayment/', LoanCalculatorView.as_view(), name='loan_repayment'),
]
