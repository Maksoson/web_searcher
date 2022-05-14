from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField


class PageContent(models.Model):
    id = models.BigAutoField('ID', primary_key=True)

    url = RichTextUploadingField('URL')
    raw_content = RichTextUploadingField('Raw page content')
    content = RichTextUploadingField('Page content')

    meta_title = RichTextUploadingField('Meta title')
    meta_description = RichTextUploadingField('Meta description')
    meta_keywords = RichTextUploadingField('Meta keywords')
    canonical = RichTextUploadingField('Canonical url')

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    def __str__(self):
        return self.meta_title

    class Meta:
        verbose_name = 'Page content'
        verbose_name_plural = 'Page content'


class Link(models.Model):
    id = models.BigAutoField('ID', primary_key=True)
    url = RichTextUploadingField('URL')
    page = models.ForeignKey('main_page.PageContent', verbose_name='Page', on_delete=models.PROTECT)

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Additional links'
        verbose_name_plural = 'Additional links'


class Word(models.Model):
    id = models.BigAutoField('ID', primary_key=True)
    value = models.CharField('Value', max_length=255)
    page = models.ForeignKey('main_page.PageContent', verbose_name='Page', on_delete=models.PROTECT)
    count = models.IntegerField('Count', default=0)

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Words'
        verbose_name_plural = 'Words'
