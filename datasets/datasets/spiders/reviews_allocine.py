import scrapy
import json
from ..items import RewiewsAllocineItem


class SpiderRewiewsAllocine(scrapy.Spider):
    # spider name
    name = "reviews_allocine"
    # url of the page to be scraped
    url = "https://www.allocine.fr/film/fichefilm-10568/critiques/spectateurs/"

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse_films)

    def parse_films(self, response):
        # print()
        cont = response.css('script[type="application/ld+json"]::text')\
            .extract_first()
        # print("Contenu JSON extrait:", cont)
        data = json.loads(cont, strict=False)
        # print("comment ", data)
        title = data['name']

        for review_data in data.get('review', []):
            review = review_data['reviewRating']['Description']
            stars = review_data['reviewRating']['ratingValue']
            stars = float(stars.replace(",", "."))

            item = RewiewsAllocineItem()
            item['title'] = title
            item['stars'] = stars
            item['review'] = review

            yield item
        # print(title)
        # print(stars)
        # print(review)
        # print()
