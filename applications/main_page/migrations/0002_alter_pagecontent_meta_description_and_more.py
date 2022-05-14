# Generated by Django 4.0.4 on 2022-05-14 17:20

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontent',
            name='meta_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Meta description'),
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='meta_keywords',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Meta keywords'),
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='meta_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Meta title'),
        ),
    ]