from django.db import models
#from django.utils.encoding import smart_str
#from docutils.core import publish_parts
class Entry(models.Model):
    """Entry Class is Main News in news app"""
    headline = models.CharField(max_length=200)
    slug = models.SlugField(unique_for_date='pub_date')
    is_active = models.BooleanField(default=False)
    pub_date = models.DateTimeField(verbose_name=("Publication date"))
    summary = models.TextField()
    summary_html = models.TextField()
    body = models.TextField()
    body_html = models.TextField()
    author = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag')
    def get_absolute_url(self):
        return "/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)
    def __unicode__(self):
        return self.headline
    def save(self, *args, **kwargs):
        #self.summary_html = publish_parts(source=smart_str(self.summary),
        #                    writer_name="html")['fragment']
        #self.body_html = publish_parts(source=smart_str(self.body),
        #                    writer_name="html")['fragment']
        self.summary = self.summary_html
        self.body = self.body_html
        super(Entry, self).save(*args, **kwargs)

class Tag(models.Model):
    """A tag menas a category"""
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    
    def __unicode__(self):
        return self.name

