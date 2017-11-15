# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy.exporters import JsonLinesItemExporter

#Pipeline to save the scraped data to a Json file
class WebScraperPipeline(object):
    def __init__(self):
        self.files = {}

    def open_spider(self, spider):
        file = open('items.jl', 'w+b')
        self.files[spider] = file
        #Use JsonLinesItemExporter since it is more reliable for bigger data set
        self.exporter = JsonLinesItemExporter(file)
        self.exporter.start_exporting()


    def close_spider(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
