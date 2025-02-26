from django import template

register = template.Library()

@register.filter
def div(value, arg):
    try:
        return float(value) / float(arg) if float(arg) != 0 else 0
    except (ValueError, ZeroDivisionError):
        return 0

@register.filter
def mul(value, arg):
    try:
        return float(value) * float(arg)
    except ValueError:
        return 0
