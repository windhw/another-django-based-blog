#when deployed ,below line should be commented
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url
from django.contrib.sitemaps import views as sitemap_views
from django.views.decorators.cache import cache_page
from .sitemaps import NewsSitemap
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
sitemaps = {
            'news': NewsSitemap,
                }
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^hellodjango/', include('hellodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^', include('rhsite.news.urls')),
    url(r'^sitemap\.xml$', cache_page(sitemap_views.sitemap, 60 * 60 * 6),
        {'sitemaps': sitemaps}),
)
urlpatterns += staticfiles_urlpatterns()
