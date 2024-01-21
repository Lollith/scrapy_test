# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RewiewsAllocineItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()  # title of the movie
    review = scrapy.Field()  # the comment
    stars = scrapy.Field()  # the stars given
