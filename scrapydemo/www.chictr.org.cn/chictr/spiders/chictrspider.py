from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import TCPTimedOutError, DNSLookupError

from ..items import ChictrItem
from ..items import ChictrDetailItem
import scrapy as scrapy
import re
from aip import AipOcr
import random
import os
import requests
from urllib import parse

class ChictrSpider(scrapy.Spider):
    name = "chictrspider"
    allowed_domains = ["www.chictr.org.cn"]
    start_urls = [
        "http://www.chictr.org.cn/searchproj.aspx"
    ]
    verify_code = ""
    client = None

    def __init__(self):
        APP_ID = '22039561'  # 刚才获取的 ID，下同
        API_KEY = 'zOGTfeDX9dVcfoQXNrvKIW2O'
        SECRECT_KEY = '8bWLRSkR7o5GqDGzSRQdmozOMEuynmMt'
        self.client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)

    def parse(self, response):
        current_page = None
        params = parse.parse_qs(parse.urlparse(response.url).query)
        if "page" in params:
            current_page = params["page"][0]
        else:
            current_page = '1'
        print("主页面 " + current_page + " 爬取成功，url ----------------------------------- ", response.url)

        trContent = response.xpath("//table[@class='table_list']/tbody/tr")
        if len(trContent) > 0:
            i = 0
            for sel in trContent:
                if i != 0:
                    item = ChictrItem()
                    item['page'] = current_page
                    item['regSite'] = sel.xpath('normalize-space(./td[3]/p[2]/text())').extract()
                    item['href'] = sel.xpath('./td[3]/p/a/@href').extract()
                    item['regNum'] = sel.xpath('normalize-space(./td[2]/text())').extract()
                    item['regTop'] = sel.xpath('normalize-space(./td[3]/p[1]/a/text())').extract()
                    item['stuType'] = sel.xpath('normalize-space(./td[4]/text())').extract()
                    item['regDate'] = sel.xpath('normalize-space(./td[5]/text())').extract()
                    yield item
                    detailurl = "http://www.chictr.org.cn/" + item['href'][0]
                    yield scrapy.Request(detailurl,
                                         callback=lambda response, page=current_page: self.get_proj_detail(response, page),
                                         errback=self.load_detail_errback)
                i = i + 1
            # 自动获取下一页的url
            next_pages = response.xpath('//div[@id="pgProj"]/a[last()-1]/@onclick').extract()[0]
            next_page_num = re.findall("\d+", next_pages)[0]
            if next_page_num is not None and int(next_page_num) < 11:
                next_page_url = "http://www.chictr.org.cn/searchproj.aspx?page=" + next_page_num + "&verifycode=" + self.verify_code
                yield scrapy.Request(next_page_url, callback=self.parse)
        else:
            print("可能需要验证码，进行验证码破解  ----------------------------------- " + response.url)
            page_btns = response.xpath('//div[@id="pgProj"]/a[last()-1]')
            if len(page_btns) < 1:
                self.verify_code = self.getVerifyCode()
                next_page_url = response.url[:response.url.index("&verifycode=")]
                yield scrapy.Request(next_page_url + "&verifycode=" + self.verify_code, callback=self.parse)

    def load_detail_errback(self, failure):
        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)
        elif failure.check(DNSLookupError):
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)
        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)

    def get_proj_detail(self, response, page):
        xml_export_url = response.xpath("//a[@class='bt_subm']/@href").extract()
        if len(xml_export_url) > 0:
            print("详情页爬取success  ----------------------------------- " + response.url)
            item = ChictrDetailItem()
            item['page'] = page
            item['trial_id'] = response.xpath(
                "normalize-space(//div[@class='ProjetInfo_ms'][1]/table/tbody/tr[1]/td[2]/text())").extract()
            item['reg_name'] = response.xpath(
                "normalize-space(//div[@class='ProjetInfo_ms'][1]/table/tbody/tr[6]/td[2]/p/text())").extract()
            item['date_registration'] = response.xpath(
                "normalize-space(//div[@class='ProjetInfo_ms'][1]/table/tbody/tr[3]/td[2]/text())").extract()
            item['study_type'] = response.xpath(
                "normalize-space(//div[@class='ProjetInfo_ms'][4]/table[1]/tbody/tr[12]/td[2]/p/text())").extract()
            item['public_title'] = response.xpath(
                "normalize-space(//div[@class='ProjetInfo_ms'][1]/table/tbody/tr[6]/td[2]/p/text())").extract()
            item['contact_name'] = response.xpath(
                "normalize-space(//div[@class='ProjetInfo_ms'][2]/table/tbody/tr[1]/td[2]/p/text())").extract()
            item['contact_telephone'] = response.xpath(
                "normalize-space(//div[@class='ProjetInfo_ms'][2]/table/tbody/tr[3]/td[2]/text())").extract()
            item['contact_email'] = response.xpath(
                "normalize-space(//div[@class='ProjetInfo_ms'][2]/table/tbody/tr[5]/td[2]/text())").extract()
            item['contact_address'] = response.xpath(
                "normalize-space(//div[@class='ProjetInfo_ms'][2]/table/tbody/tr[7]/td[2]/p/text())").extract()
            item['agemin'] = response.xpath(
                "normalize-space(//div[@class='ProjetInfo_ms'][9]/table/tbody/tr[1]/td[4]/table/tbody/tr[1]/td[2]/text())").extract()
            item['agemax'] = response.xpath(
                "normalize-space(//div[@class='ProjetInfo_ms'][9]/table/tbody/tr[1]/td[4]/table/tbody/tr[2]/td[2]/text())").extract()
            item['gender'] = response.xpath(
                "normalize-space(//div[@class='ProjetInfo_ms'][9]/table/tbody/tr[2]/td[2]/p/text())").extract()
            item['inclusion_criteria'] = response.xpath(
                "normalize-space(//div[@class='ProjetInfo_ms'][4]/table[1]/tbody/tr[22]/td[2]/p/text())").extract()
            item['exclusion_criteria'] = response.xpath(
                "normalize-space(//div[@class='ProjetInfo_ms'][4]/table[1]/tbody/tr[24]/td[2]/p/text())").extract()
            yield item
        else:
            print("IP可能被封，获取新IP再次进行详情页数据爬取  ----------------------------------- " + response.url)
            yield scrapy.Request(response.url,
                                 callback=lambda response, page=page: self.get_proj_detail(response, page))

    def getVerifyCode(self):
        rand = random.random()
        url = "http://www.chictr.org.cn/Tools/verifyimagepage.aspx?textcolor=2&bgcolor=F4F4F4&ut=1&time=" + str(rand)

        # 设置文件和文件名
        filename = "verifycode.png"
        filepath = os.path.join(os.curdir, filename)
        # 发送请求保存图片
        resp = requests.get(url)
        with open(filepath, "wb") as f:
            for chunk in resp.iter_content(1024):
                f.write(chunk)

        # 带参数调用通用文字识别
        image = self.get_file_content('verifycode.png')
        general = self.client.basicGeneral(image)

        # 处理得到的words
        words = ""
        if len(general["words_result"]) > 0:
            words = general["words_result"][0]["words"]
        words = words.replace(" ", "")
        print("识别内容为 ----------------------------------- ", words)
        return words

    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
