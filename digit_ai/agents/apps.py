from django.apps import AppConfig


class AgentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'digit_ai.agents'  # Update to reflect proper namespace


class BudgetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'digit_ai.budget'  # Update to reflect proper namespace