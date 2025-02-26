from django import template

register = template.Library()

@register.filter
def div(value, arg):
    try:
        return float(value) / float(arg) if float(arg) != 0 else 0
    except (ValueError, TypeError):
        return 0

@register.filter
def mul(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def percentage(value, arg):
    """
    Calculates percentage with safeguards
    Usage: {{ value|percentage:max_value }}
    """
    try:
        if float(arg) == 0:
            return 0
        result = (float(value) / float(arg)) * 100
        return min(result, 100)  # Cap at 100%
    except (ValueError, TypeError):
        return 0