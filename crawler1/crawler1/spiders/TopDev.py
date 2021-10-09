import scrapy
from crawler1.items import Crawler1Item


class TopdevSpider(scrapy.Spider):
    name = 'TopDev'
    # allowed_domains = ['https://topdev.vn/blog/motion-graphics-design-la-gi/']
    start_urls = ['https://topdev.vn/blog/category/lap-trinh/mobile/']

    def parse(self, response):
        listLink = response.css('#td-outer-wrap > div.td-main-content-wrap.td-container-wrap > div > div > div.td-pb-span8.td-main-content > div > div:nth-child(2) > div.td-module-thumb > a::attr(href)').extract()

        print(listLink)

    #     for link in listLink:
    #         yield scrapy.Request(link, callback=self.crawlData)

    # def crawlData(self, response):
    #     # print(response.url)
    #     # print(response.css('#ftwp-postcontent > p:nth-child(1)').extract())
    #     # print(response.css('title::text').extract())

    #     item = Crawler1Item()

    #     item['link'] = response.url 
    #     item['title'] = response.css('title::text').extract()
    #     item['about'] = response.css('#ftwp-postcontent > p:nth-child(1) > span:nth-child(1)::text').extract()

    #     print(item)
