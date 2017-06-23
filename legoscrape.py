import scrapy


class legoSpider(scrapy.Spider):
    name = 'lego_spider'
    startYear = '2014'
    start_urls = ['http://brickset.com/sets/year-' + startYear]
    

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h1 a ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd/a/text()'
            PRICE_SELECTOR = './/dl[dt/text() = "RRP"]/dd/text()'
            YEAR_SELECTOR = '//*[@id="banner"]/div/nav[2]/ul/li[4]/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'

            yield {'name': brickset.css(NAME_SELECTOR).extract_first(),
                   'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                   'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                   'price': brickset.xpath(PRICE_SELECTOR).extract_first(),
                   'image': brickset.css(IMAGE_SELECTOR).extract_first(),
                   'year': brickset.xpath(YEAR_SELECTOR).extract_first(),
                   'pageURL': response.url,}

            NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            NEXT_YEAR_SELECTOR = '#body > div.outerwrap > div > div > aside:nth-child(2) > div > div:nth-child(3) > a ::attr(href)'
            
            if next_page:
                yield scrapy.Request(response.urljoin(next_page), callback = self.parse)
            else:
                next_year = response.css(NEXT_YEAR_SELECTOR).extract_first()
                yield scrapy.Request(response.urljoin(next_year), callback = self.parse)
                
                


            
    
