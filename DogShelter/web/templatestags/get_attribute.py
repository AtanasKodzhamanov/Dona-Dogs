from django import template

register = template.Library()

@register.filter
def getattribute(value, arg):
    if hasattr(value, arg):
        return getattr(value, arg)
    else:
        return None
