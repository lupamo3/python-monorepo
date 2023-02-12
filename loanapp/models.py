from django.db import models

class Loan(models.Model):
    LOAN_REPAYMENT_FREQUENCY_CHOICES = (
        ('monthly', 'Monthly'),
        ('bi-monthly', 'Bi-monthly'),
        ('weekly', 'Weekly'),
    )

    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_term_months = models.IntegerField()
    interest_rate_per_year = models.DecimalField(max_digits=5, decimal_places=2)
    repayment_frequency = models.CharField(max_length=20, choices=LOAN_REPAYMENT_FREQUENCY_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Loan {self.pk}"
