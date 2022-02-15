import scrapy
from scrapy.linkextractors import LinkExtractor

class Jianshu(scrapy.Spider):
    name = "jianshu_spider"
    allowed_domains = ["isrctn.com"]

    def __init__(self, *args, **kwargs):
        super(Jianshu, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.isrctn.com/search?q=&filters=GT+lastEdited:2020-10-28T00:00:00.000Z,LE+lastEdited:2020-10-29T00:00:00.000Z&page=1&pageSize=100&searchType=advanced-search']

    def parse(self, response):
        link = LinkExtractor(allow=r'ISRCTN\d+',)
        links = link.extract_links(response)
        if links:
            for link_one in links:
                print(link_one.url)