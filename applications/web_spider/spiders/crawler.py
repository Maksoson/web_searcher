from scrapy.spiders import CrawlSpider, Rule

from common.scripts.text_cleaners import clean
from scrapy.linkextractors import LinkExtractor

from applications.web_spider.items import PageContentItem


class CrawlerSpider(CrawlSpider):
    name = 'crawler'
    base_url = 'https://habr.com'
    start_urls = ['https://habr.com/ru/all/']

    rules = (
        Rule(LinkExtractor(), callback='parse', follow=True),
    )

    def parse(self, response, **kwargs):
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

        yield dict(page_content)
