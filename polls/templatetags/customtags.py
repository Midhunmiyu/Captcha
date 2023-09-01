from django import template
from polls.forms import CaptchaForm


register = template.Library()

@register.simple_tag
def getcapcheform():
    return CaptchaForm()