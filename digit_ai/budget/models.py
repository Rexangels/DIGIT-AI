from django.db import models

# Create your models here.
# budget/models.py
class BudgetTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('api_call', 'API Call'),
        ('storage', 'Storage'),
        ('processing', 'Processing'),
    ]
    
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=6)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    agent = models.ForeignKey('agents.Agent', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"