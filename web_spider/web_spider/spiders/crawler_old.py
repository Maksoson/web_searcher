import scrapy

from functions.cleaner import clean_text
import applications.main_page.models as main_page_models
import applications.logs.models as logs_models
from scrapy.linkextractors import LinkExtractor


class CrawlerOldSpider(scrapy.Spider):
    name = 'crawler_old'
    base_url = 'https://habr.com'
    start_urls = ['https://habr.com/ru/all/']
    depth = 1
    max_depth = 6
    link_extractor = LinkExtractor()

    def parse(self, response, **kwargs):
        for link in self.link_extractor.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_detail)

    def parse_detail(self, response):
        page_body = response.css('body')

        raw_content = page_body.get()
        content = clean_text(raw_content)

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

        defaults = {
            'url': response.url,
            'raw_content': raw_content,
            'content': content,

            'meta_title': meta_title,
            'meta_description': meta_description,
            'meta_keywords': meta_keywords,
            'canonical': canonical
        }
        try:
            main_page_models.PageContent.objects.update_or_create(
                url=response.url,
                defaults=defaults
            )
        except Exception as error:
            self.logger.info('Crawl ' + response.url + ' error! ' + str(error))
            logs_models.Log.objects.create(text='Crawl ' + response.url + ' error! ' + str(error))

        if self.depth < self.max_depth:
            self.depth = self.depth + 1
            links = page_body.css('a::attr(href)').getall()

            for link in links:
                yield scrapy.Request(link, callback=self.parse_detail)

        yield dict(defaults)
