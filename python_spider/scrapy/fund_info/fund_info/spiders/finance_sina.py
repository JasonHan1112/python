import scrapy


class FinanceSinaSpider(scrapy.Spider):
    name = 'finance_sina'
    allowed_domains = ['finance.sina.com.cn']
    start_urls = ['http://finance.sina.com.cn/']

    def parse(self, response):
        pass
