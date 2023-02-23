from django import template

register = template.Library()


@register.filter
def getattribute(value, arg):
    print("value: ", value)
    print("arg: ", arg)
    if hasattr(value, arg):
        print("returned value: ", getattr(value, arg))
        return getattr(value, arg)
    else:
        print("returned none")
        return None
