from django.db import models


class PageContent(models.Model):
    id = models.BigAutoField('ID', primary_key=True)

    url = models.TextField('URL', db_index=True)
    raw_content = models.TextField('Raw page content', default='', blank=True)
    content = models.TextField('Page content', default='', blank=True)

    meta_title = models.TextField('Meta title', default='', blank=True)
    meta_description = models.TextField('Meta description', default='', blank=True)
    meta_keywords = models.TextField('Meta keywords', default='', blank=True)
    canonical = models.TextField('Canonical url', default='', blank=True)

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    def __str__(self):
        return self.meta_title

    class Meta:
        verbose_name = 'Page content'
        verbose_name_plural = 'Page content'


class Word(models.Model):
    id = models.BigAutoField('ID', primary_key=True)
    value = models.CharField('Value', max_length=255, db_index=True)
    page = models.ForeignKey('main_page.PageContent', verbose_name='Page', on_delete=models.PROTECT)
    count = models.IntegerField('Count', default=0)

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Words'
        verbose_name_plural = 'Words'
