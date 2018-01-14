from django import template
from poll.models import Status

register = template.Library()

''' Sprawdza czy głosowanie się już zakończyło i czy można podawać wyniki '''
@register.simple_tag
def is_poll_active():
    out = Status.objects.get(id = 1).poll_status
    return out 
