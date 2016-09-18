import scrapy
from fintech_guardian.items import FintechNytimesItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from fintech_guardian.get_guardian import get_guardian_time_words
from fintech_guardian.csv_write import write_csv
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class FinNewsSpider(CrawlSpider):
    name = "guardian"
    allowed_domains = ["theguardian"]
    url = ""
    start_urls = []

    for i in range(1, 13):
        url = 'https://www.theguardian.com/technology/ipod?page={}'.format(i)
        start_urls.append(url)

    def parse(self, response):
        item = FintechNytimesItem()
        try:
            for subitem in response.xpath('//div[@class="fc-item__container"]/a'):
                news = {}
                time, words = get_guardian_time_words(subitem.extract())
                news[str(time)] = words
                write_csv(news)
        except Exception, e:
            pass
