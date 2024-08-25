import scrapy


class ContohSpider(scrapy.Spider):
    name = "contoh"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
