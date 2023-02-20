from django import template
from django import template

register = template.Library()


@register.filter
def field_loop(dictionary, key):
    return dictionary.get(key)
