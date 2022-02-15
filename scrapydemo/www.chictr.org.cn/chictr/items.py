# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChictrItem(scrapy.Item):
    page = scrapy.Field()
    regSite = scrapy.Field()
    href = scrapy.Field()
    regNum = scrapy.Field()
    regTop = scrapy.Field()
    stuType = scrapy.Field()
    regDate = scrapy.Field()


class ChictrDetailItem(scrapy.Item):
    page = scrapy.Field()
    trial_id = scrapy.Field()
    reg_name = scrapy.Field()
    date_registration = scrapy.Field()
    study_type = scrapy.Field()
    public_title = scrapy.Field()
    contact_name = scrapy.Field()
    contact_address = scrapy.Field()
    contact_telephone = scrapy.Field()
    contact_email = scrapy.Field()
    inclusion_criteria = scrapy.Field()
    agemin = scrapy.Field()
    agemax = scrapy.Field()
    gender = scrapy.Field()
    exclusion_criteria = scrapy.Field()
