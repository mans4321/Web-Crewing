import scrapy
import lxml.html
from scrapy.loader import ItemLoader

from web_scraper.items import WebScrapingItem

# To run the spider: scrapy crawl concordia

class WebSpider(scrapy.Spider):
    # The name of the spider which is used when running it
    name = "concordia"
    # the crawler will look at these urls as the starting point
    start_urls = [
        "http://cufa.net",
        "http://concordia.ca"
        ]

    # The parse function will be implicitly called after response from the site
    def parse(self, response):
        print('-------------------')
        # Will get the text content of all tags, except for the script tag, which would be javascript code
        res_list = response.xpath('//html//text()[not(parent::script)]').extract()
        parsed_text_list = []
        for text in res_list:
            # Removes excess tabs or line breaks
            text = text.strip()
            # Will only keep values that are not empty. The @media check is to remove some css that got extracted
            if(text != "" and "@media" not in text):
                parsed_text_list.append(text)
        print('-------------------')

        # These items are defined in the items.py file
        l = ItemLoader(item=WebScrapingItem(), response=response)
        l.add_value('name', response.url)
        l.add_value('content', parsed_text_list)

        yield l.load_item()

        for href in response.css('a::attr(href)'):
            yield response.follow(href, callback=self.parse)

