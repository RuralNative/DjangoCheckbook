from django.db import models

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    starting_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Transaction(models.Model):
    DATE_FORMAT = '%Y-%m-%d'

    date = models.DateField()
    transaction_type = models.CharField(max_length=20, choices=[('deposit', 'Deposit'), ('withdrawal', 'Withdrawal')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"Transaction on {self.date}: {self.get_transaction_type_display()} ${self.amount}"