import scrapy
from fund_info.items import FundInfoItem

class FinanceSinaSpider(scrapy.Spider):
    name = 'finance_sina'
    allowed_domains = ['finance.sina.com.cn']

    def start_requests(self):
        urls = [
                #'https://finance.sina.com.cn/roll/index.d.html?cid=56942&page=1'
                'http://finance.sina.com.cn/roll/index.d.html?cid=56934&page=1'
               ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_fund_comment)

    def parse_fund_comment(self, response):
        #fund_comment_item = FundInfoItem()
        fund_comment_items = []
        self.logger.info("this is parse_fund_comment, will parse fund comment")
        for title in response.xpath('//ul[@class="list_009"]/li'):
            #self.logger.info("")
            #self.logger.info(title.xpath('./a/text()').get())
            #self.logger.info(title.xpath('./span/text()').get())
            fund_comment_item = {}
            fund_comment_item['title'] = title.xpath('./a/text()').get()
            fund_comment_item['date'] = title.xpath('./span/text()').get()
            fund_comment_item['html'] = title.xpath('./a/@href').get()
            fund_comment_items.append(fund_comment_item)
        #self.logger.info(fund_comment_items)
        for item in fund_comment_items:
            print(item['title']+item['date']+'\t\t\t'+item['html'])


    def parse(self, response):
        pass
