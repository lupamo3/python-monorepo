from rest_framework import serializers

class LoanCalculatorSerializer(serializers.Serializer):
    loan_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    loan_term = serializers.IntegerField()
    interest_rate = serializers.DecimalField(max_digits=5, decimal_places=2)
    repayment_frequency = serializers.ChoiceField(choices=["monthly", "bi-monthly", "weekly"])
