from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from decimal import Decimal

from .serializers import LoanCalculatorSerializer

class LoanCalculatorView(APIView):
    serializer_class = LoanCalculatorSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract input parameters
        loan_amount = serializer.validated_data["loan_amount"]
        loan_term = serializer.validated_data["loan_term"]
        interest_rate = serializer.validated_data["interest_rate"]
        repayment_frequency = serializer.validated_data["repayment_frequency"]

        # Calculate interest rate per period based on repayment frequency
        if repayment_frequency == "monthly":
            interest_rate_per_period = interest_rate / 12
        elif repayment_frequency == "bi-monthly":
            interest_rate_per_period = interest_rate / 24
        elif repayment_frequency == "weekly":
            interest_rate_per_period = interest_rate / 52

        # Calculate monthly payment
        r = Decimal(interest_rate_per_period) / Decimal(100)
        n = Decimal(loan_term)
        p = Decimal(loan_amount)
        monthly_payment = (r * p) / (1 - ((1 + r) ** (-n)))

        # Initialize variables for calculating loan breakdown
        interest_paid = Decimal(0)
        principal_paid = Decimal(0)
        remaining_balance = Decimal(loan_amount)
        loan_breakdown = []

        # Calculate loan breakdown for each repayment period
        for i in range(loan_term):
            interest = remaining_balance * (r / Decimal(12))
            principal = monthly_payment - interest
            remaining_balance -= principal

            # Add breakdown to list
            loan_breakdown.append({
                "period": i+1,
                "principal": round(principal, 2),
                "interest": round(interest, 2),
                "remaining_balance": round(remaining_balance, 2)
            })

            # Update total interest and principal paid
            interest_paid += interest
            principal_paid += principal

        # Calculate total amount to be repaid
        total_amount = loan_amount + interest_paid

        # Return loan breakdown and summary information
        response_data = {
            "total_interest_paid": round(interest_paid, 2),
            "total_amount_to_repay": round(total_amount, 2),
            "loan_breakdown": loan_breakdown
        }

        return Response(response_data, status=status.HTTP_200_OK)
