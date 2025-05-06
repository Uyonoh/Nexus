import re
from django import template

register = template.Library()

@register.filter
def regex_replace(value, arg):
    pattern, repl = arg.split(',', 1)
    return re.sub(pattern, repl, value)
