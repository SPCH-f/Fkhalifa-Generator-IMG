from django import template

register = template.Library()

@register.filter
def lookup(dictionary, key):
    """
    Custom template filter for dictionary lookup
    Usage: {{ dict|lookup:key }}
    """
    if dictionary is None:
        return ''
    return dictionary.get(key, '')
