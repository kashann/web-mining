# -*- coding: utf-8 -*-
import scrapy


class Amazon10Spider(scrapy.Spider):
    name = 'amazon10'
    allowed_domains = ['amazon.com']
    # Smart Lighting category
    start_urls = ['https://www.amazon.com/gp/browse.html?node=13575748011&ref_=nav_em_0_2_8_3_sbdshd_lighting']
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64;     x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    def parse(self, response):      
        for link in response.css('a.a-link-normal.s-access-detail-page'):
            yield scrapy.Request(url = link.xpath('@href').extract_first(), callback = self.parse_product, headers = self.headers)
    
    def parse_product(self, response):
        title = response.css('span#productTitle').xpath('text()').get()
        price = response.css('span#price_inside_buybox').xpath('text()').get()
        description = response.xpath('//ul[@class="a-unordered-list a-vertical a-spacing-mini"]//li//span//text()').getall()
        secondReview = response.css('span.a-size-base.a-color-tertiary.cr-vote-text').xpath('text()').extract()[1]
        print(title)
        print(price)
        print(description)
        print(secondReview)
