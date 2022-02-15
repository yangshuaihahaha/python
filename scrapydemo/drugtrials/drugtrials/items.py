# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DrugtrialsItem(scrapy.Item):
    # define the fields for your item here like:
    num = scrapy.Field()
    reg_num = scrapy.Field()
    status = scrapy.Field()
    drug_name = scrapy.Field()
    indications = scrapy.Field()
    topic = scrapy.Field()

class DrugtrialsDetailItem(scrapy.Item):
    trial_id = scrapy.Field()
    drug_name = scrapy.Field()
    indications = scrapy.Field()
    topic = scrapy.Field()

    applicant = scrapy.Field()
    contact_name = scrapy.Field()
    contact_num = scrapy.Field()
    contact_phone = scrapy.Field()
    contact_email = scrapy.Field()
    contact_address = scrapy.Field()

    age = scrapy.Field()
    gender = scrapy.Field()
    inclusion_criteria = scrapy.Field()
    exclusion_criteria = scrapy.Field()

