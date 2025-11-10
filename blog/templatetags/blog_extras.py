# blog/templatetags/blog_extras.py

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# These custom tags help with Bootstrap-like layout blocks

@register.simple_tag
def row(classes=""):
    """Start a Bootstrap row with optional classes."""
    return mark_safe(f'<div class="row {classes}">')

@register.simple_tag
def endrow():
    """End a Bootstrap row."""
    return mark_safe('</div>')

@register.simple_tag
def col(classes=""):
    """Start a Bootstrap column with optional classes."""
    return mark_safe(f'<div class="col {classes}">')

@register.simple_tag
def endcol():
    """End a Bootstrap column."""
    return mark_safe('</div>')
