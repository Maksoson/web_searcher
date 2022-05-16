# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from applications.main_page.models import PageContent
from applications.web_spider.items import PageContentItem
from applications.logs.models import Log


class ScrapyAppPipeline(object):
    def process_item(self, item: PageContentItem, spider):
        try:
            PageContent.objects.update_or_create(
                url=item['url'],
                defaults=item
            )
        except Exception as error:
            Log.objects.create(text='Crawl ' + item['url'] + ' error! ' + str(error))

        return item
