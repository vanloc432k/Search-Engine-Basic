import scrapy
from crawler1.items import Crawler1Item


class TopdevSpider(scrapy.Spider):
    name = 'TopDev'
    # allowed_domains = ['https://topdev.vn/blog/motion-graphics-design-la-gi/']
    start_urls = ['https://topdev.vn/blog/category/lap-trinh/ai-machine-learning/#',
    'https://topdev.vn/blog/category/lap-trinh/mobile/#',
    'https://topdev.vn/blog/category/lap-trinh/frontend/#',
    'https://topdev.vn/blog/category/lap-trinh/backend/#',
    'https://topdev.vn/blog/category/lap-trinh/fullstack/#',
    'https://topdev.vn/blog/category/lap-trinh/product/#',
    'https://topdev.vn/blog/category/lap-trinh/devops/#',
    'https://topdev.vn/blog/category/cong-nghe/#',
    'https://topdev.vn/blog/category/chuyen-gia-noi/#',
    'https://topdev.vn/blog/category/phong-van/#']

    def parse(self, response):
        listLink = response.css('div.td_module_10.td_module_wrap.td-animation-stack > div.item-details > h3 > a::attr(href)').extract()

        # print(listLink)

        for link in listLink:
            yield scrapy.Request(link, callback=self.crawlData)

    def crawlData(self, response):
        # print(response.url)
        # print(response.css('#ftwp-postcontent > p:nth-child(1)').extract())
        # print(response.css('title::text').extract())

        item = Crawler1Item()

        item['link'] = str(response.url) 
        item['title'] = str(response.css('head > title::text').extract_first())
        item['about'] = str(response.css('#ftwp-postcontent > p > span::text').extract_first())

        print(item)
        yield item 

        listSubLink = response.css('div.td-related-span4 > div > div.td-module-image > div.td-module-thumb > a::attr(href)').extract()

        # print(listLink)

        for link in listSubLink:
            yield scrapy.Request(link, callback=self.crawlData)
