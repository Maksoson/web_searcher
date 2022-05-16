import scrapy

from common.scripts.text_cleaners import clean
import applications.main_page.models as main_page_models
import applications.logs.models as logs_models
from applications.web_spider.items import PageContentItem
from applications.main_page.models import PageContent


class SinglePageSpider(scrapy.Spider):
    """ This crawler re-crawling the oldest 1000 pages by timetable """
    name = 'single_page'
    re_crawl_page_count = 1000

    def parse(self, response, **kwargs):
        for page in PageContent.objects.order_by('updated_at').get()[:self.re_crawl_page_count]:
            yield scrapy.Request(page.url, callback=self.parse_detail)

    def parse_detail(self, response):
        page_body = response.css('body')

        raw_content = page_body.get()
        content = raw_content

        meta_title = response.css('title::text').get()
        if meta_title is None:
            meta_title = ''
        meta_description = response.xpath("//meta[@name='description']/@content").get()
        if meta_description is None:
            meta_description = ''
        meta_keywords = response.xpath("//meta[@name='keywords']/@content").get()
        if meta_keywords is None:
            meta_keywords = ''
        canonical = response.xpath("//link[@rel='canonical']/@href").get()
        if canonical is None:
            canonical = ''

        page_content = PageContentItem()
        page_content['url'] = response.url
        page_content['raw_content'] = raw_content
        page_content['content'] = clean(content)
        page_content['meta_title'] = clean(meta_title)
        page_content['meta_description'] = clean(meta_description)
        page_content['meta_keywords'] = clean(meta_keywords)
        page_content['canonical'] = canonical

        try:
            main_page_models.PageContent.objects.update_or_create(
                url=response.url,
                defaults=page_content
            )
        except Exception as error:
            self.logger.info('Crawl ' + response.url + ' error! ' + str(error))
            logs_models.Log.objects.create(text='Crawl ' + response.url + ' error! ' + str(error))

        yield dict(page_content)
