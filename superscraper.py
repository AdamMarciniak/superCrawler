import scrapy


class superSpider(scrapy.Spider):
    name = 'super_spider'
    start_urls = ['https://www.realcanadiansuperstore.ca/Food/Fruits-%26-Vegetables/Fruit/c/RCSS001001001000']

    def parse(self, response):

        CAT_LINK_SELECTOR = 'li::attr(data-level="3") > a::attr(href) '

        for catLink in response.css(CAT_LINK_SELECTOR):

            yield response.follow(catLink, self.parse_item)



    def parse_item(self, response):
        
        ITEM_SELECTOR = '#content > div.page-subcategory > div > div.wrapper-category > div.page-subcategory > div:nth-child(4) > div > div > div > div > div > div > div'

        for itemset in response.css(ITEM_SELECTOR):

            LINK_SELECTOR = 'div > div > div:nth-child(3) > div > a ::attr(href)'

            itemLink = itemset.css(LINK_SELECTOR).extract_first()

            yield response.follow(itemLink, self.parse_nutri)

            
            

    def parse_nutri(self, response):


        NAME_SELECTOR = '#content > div.page-product-display.product-display-page.container > div > div > div > div.row.wrapper-product-info > div.module-product-info > div > div.row-product-name.row > div.col-sm-10.col-md-8.col-lg-12 > h1::text'
        TOTAL_FAT_NAME_SELECTOR = '#nutrition > div > div.wrapper-nutrition-label-inner > div > div.row-nutrition-fact-attr.hidden-sm.row > div.nutrition-fact-attr-left > div:nth-child(2) > span.nutrition-label ::text'
        TOTAL_FAT_VAL_SELECTOR = '#nutrition > div > div.wrapper-nutrition-label-inner > div > div.row-nutrition-fact-attr.hidden-sm.row > div.nutrition-fact-attr-left > div:nth-child(2)::text'
        yield {'name' : ''.join(response.css(NAME_SELECTOR).extract()).strip(),
               response.css(TOTAL_FAT_NAME_SELECTOR).extract_first().strip() : ''.join(response.css(TOTAL_FAT_VAL_SELECTOR).extract()).strip()}
        
            

            
            
