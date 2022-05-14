from django.contrib import admin

from applications.main_page.models import PageContent


class PageContentAdmin(admin.ModelAdmin):
    fields = ['id', 'url', 'raw_content', 'content', 'meta_title', 'meta_description', 'meta_keywords', 'canonical',
              'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']

    search_fields = []
    list_display = ['id', 'url', 'meta_title', 'created_at', 'updated_at']

    filter_horizontal = []
    list_filter = []
    fieldsets = []


admin.site.register(PageContent, PageContentAdmin)
