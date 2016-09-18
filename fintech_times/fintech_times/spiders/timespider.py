import scrapy
from fintech_times.items import FintechTimesItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class FinNewsSpider(CrawlSpider):
    name = "times"
    allowed_domains = ["www.thetimes.co.uk"]
    url = ""
    start_urls = []

    for i in range(1, 10):
        url = "http://www.thetimes.co.uk/search?p={}&q=iphone".format(i)
        start_urls.append(url)

    def parse(self, response):
        item = FintechTimesItem()
        itemlist = []
        try:
            for ele in response.xpath('//h2[@class="Item-headline Headline--s Headline--regular"]'):
                title = ele.xpath('a').extract()
                date = ele.xpath('../div/span[@class="Dateline Item-dateline"]/text()').extract()
                print("{}:{}".format(date, title))
            item["news"] = itemlist
        except Exception, e:
            pass

