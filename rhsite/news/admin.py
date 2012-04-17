from django.contrib import admin
from .models import Entry,Tag
class EntryAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js',
                '/static/js/textarea.js',)
    list_display = (
            'headline',
            'pub_date',
            'is_active',
            'author')
    list_filter = ('is_active',)
    exclude = ('summary', 'body')
    prepopulated_fields = {"slug": ("headline",)}
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(EntryAdmin,self).formfield_for_dbfield(db_field,**kwargs)
        if db_field.name == 'body':
            formfield.widget.attrs['rows']= 25
        return formfield

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Entry,EntryAdmin)
admin.site.register(Tag,TagAdmin)
