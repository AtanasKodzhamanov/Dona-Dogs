from django import template

register = template.Library()


@register.filter
def truncatetext(value, arg):
    try:
        length = int(arg)
    except ValueError:
        return value

    if len(value) > length:
        truncated = value[:length]
        if not truncated.endswith(" "):
            truncated = truncated[:truncated.rindex(" ")]
        truncated = truncated.rstrip()
        truncated = truncated.rstrip(".")
        truncated = truncated.rstrip(",")
        truncated = truncated + "..."

        return truncated
    else:
        return value
