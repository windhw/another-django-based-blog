# Create your views here.
import functools
from django.views.generic import date_based
from django.views.generic import list_detail
from .models import Entry,Tag

def prepare_arguments(view):
    @functools.wraps(view)
    def wrapped(request, *args, **kwargs):
        kwargs['allow_future'] = True
        kwargs['queryset'] = Entry.objects.all()
        kwargs['date_field'] = 'pub_date'
        return view(request, *args, **kwargs)
    return wrapped

@prepare_arguments
def entry_detail(request, *args, **kwargs):
    return date_based.object_detail(request, *args, **kwargs)

@prepare_arguments
def archive_day(request, *args, **kwargs):
    return date_based.archive_day(request, *args, **kwargs)

@prepare_arguments
def archive_month(request, *args, **kwargs):
    return date_based.archive_month(request, *args, **kwargs)

@prepare_arguments
def archive_year(request, *args, **kwargs):
    return date_based.archive_year(request, *args, **kwargs)

@prepare_arguments
def archive_index(request, *args, **kwargs):
    return date_based.archive_index(request, *args, **kwargs)


def tag_list(request, *args, **kwargs):
    kwargs['paginate_by'] = 5
    tag = '';
    if kwargs.has_key('tag'):
        tag = kwargs['tag']
        del kwargs['tag']
    q = Tag.objects.all().filter(slug=tag)
    if q:
        kwargs['queryset'] = q.get().entry_set.all()
        kwargs['extra_context'] = {'tag':q.get()}
    else:
        kwargs['queryset'] = q
    return list_detail.object_list(request, *args, **kwargs)
