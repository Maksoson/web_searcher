from django.db import models


TOURNAMENT_TYPES = [
    ['crawler', 'Crawler process'],
    ['text_indexing', 'Text indexing process'],
]


class Log(models.Model):
    id = models.BigAutoField('ID', primary_key=True)
    type = models.CharField('Type', max_length=255, choices=TOURNAMENT_TYPES)
    text = models.TextField('Reason', default='', blank=True)

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Logs'
        verbose_name_plural = 'Logs'
