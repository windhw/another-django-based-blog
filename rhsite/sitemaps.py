from django.contrib.sitemaps import Sitemap
from .news.models import Entry
class NewsSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.4
    def items(self):
        return Entry.objects.all()
