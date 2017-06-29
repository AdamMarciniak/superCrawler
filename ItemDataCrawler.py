import scrapy

with open(r'C:\Users\amarciniak\Desktop\PythonPrograms\crawler\links.txt') as f:
    lines = f.read().splitlines()


class superScraper(scrapy.Spider):
    name = "spidey"
    start_urls = lines

    custom_settings = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        for i, url in enumerate(self.start_urls):
            yield scrapy.Request(url, cookies={'currentRegion': 'CA-BC'}, callback=self.parse_item, headers=headers)


    def parse_item(self, response):
        self.log('I just visited: ' + response.url)
        yield{
            'item_name': ('').join(response.css('h1.product-name::text').extract()).strip(),
            'calories': response.css('#nutrition > div > div.wrapper-nutrition-label-inner > div > div.row-nutrition-fact-summary.row > div:nth-child(4) > span.nutrition-summary-value::text').extract_first().strip(' >\n\t</span>;'),
        }

