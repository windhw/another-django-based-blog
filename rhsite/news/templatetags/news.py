from __future__ import absolute_import

from django import template
from ..models import Entry,Tag
from django.db.models import Count

register = template.Library()

@register.inclusion_tag('news/sidebar.html')
def render_sidebar():
    return {
        'dates': Entry.objects.all().dates('pub_date', 'month'),
        'tags':  Tag.objects.all().annotate(num_entry = Count('entry')),
    }

@register.filter
def get_month(value):
    return value.strftime("%b").lower()


