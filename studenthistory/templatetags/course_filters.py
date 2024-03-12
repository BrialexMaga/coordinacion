from django import template

register = template.Library()

@register.filter
def is_failed(grade):
    try:
        return float(grade) < 60
    except ValueError:
        return grade == 'SD'