import scrapy

class QouteSpider(scrapy.Spider):
    # first initialize the name and start_url
    name = 'qoutes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # fetching website title
        # title::text allows only to scrap the title text without the tags
        title = response.css('title::text').extract()
        yield { 'title_txt' : title }