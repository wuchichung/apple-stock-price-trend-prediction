import scrapy
from fintech_bloomberg.items import FintechItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from csv_write import write_csv
from fintech_bloomberg.tools import get_time_words

class FinNewsSpider(CrawlSpider):
    name = "finnews"
    allowed_domains = ["bloomberg"]
    url = ""
    start_urls = []

    for i in range(1, 3001):
        url = 'http://www.bloomberg.com/search?query=apple&page={}'.format(i)
        start_urls.append(url)

    def parse(self, response):
        item = FintechItem()

        for subitem in response.xpath('//article[contains(@class, "search-result-story")]/div'):
            title = subitem.xpath('h1[@class="search-result-story__headline"]/a').extract()
            time = subitem.xpath('div/span/time[@class="published-at"]/text()').extract()
            # print('{} : {}'.format(title, time))
            news = {}
            news[str(time)] = title
            # print(get_time_words(news))
            write_csv(get_time_words(news))

            # item["title"] = get_time_words(response.xpath('//article[@class="search-result-story type-article"]/'
            #                                'div/h1[@class="search-result-story__headline"]/a').extract())
            # item["date"] = response.xpath('//article[@class="search-result-story type-article"]/'
            #                               'div/div/span/time[@class="published-at"]/text()').extract()
            # return item
