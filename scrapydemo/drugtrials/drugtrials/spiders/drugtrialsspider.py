from ..items import DrugtrialsItem
from ..items import DrugtrialsDetailItem
import scrapy as scrapy
import re
from urllib import parse
from selenium import webdriver
from lxml.html import fromstring

class DrugtrialsSpider(scrapy.Spider):
    name = "drugtrialsspider"
    allowed_domains = ["www.chinadrugtrials.org.cn"]
    start_urls = [
        "http://www.chinadrugtrials.org.cn/clinicaltrials.searchlist.dhtml"
    ]
    home_page_cookie = ""
    detail_page_cookie = ""
    proxy = 'http://18.130.89.239:80'

    def parse(self, response):
        current_page = None
        params = parse.parse_qs(parse.urlparse(response.url).query)
        if "currentpage" in params:
            current_page = params["currentpage"][0]
        else:
            current_page = '1'
        if response.status == 200:
            homeContent = response.xpath("//table[@class='searchTable']//tr[position()>1]")
            if len(homeContent) > 0:
                print("主页面 " + current_page + " 爬取成功，url ----------------------------------- ", response.url)
                # 获取主页数据
                for sel in homeContent:
                    item = DrugtrialsItem()
                    item['num'] = sel.xpath('normalize-space(./td[1]/text())').extract()[0]
                    item['reg_num'] = sel.xpath('normalize-space(./td[2]/a/text())').extract()[0]
                    item['status'] = sel.xpath('normalize-space(./td[3]/a/text())').extract()[0]
                    item['drug_name'] = sel.xpath('normalize-space(./td[4]/a/text())').extract()[0]
                    item['indications'] = sel.xpath('normalize-space(./td[5]/a/text())').extract()[0]
                    item['topic'] = sel.xpath('normalize-space(./td[6]/a/text())').extract()[0]
                    yield item
                    yield scrapy.Request(
                        "http://www.chinadrugtrials.org.cn/clinicaltrials.searchlistdetail.dhtml?currentpage=" +
                        str(item['num']).strip(), cookies=self.detail_page_cookie, callback=self.get_detail)
                # 自动获取下一页的url
                next_pages = response.xpath('//ul[@class="pagination"]/li[last()]/a/@onclick').extract()[0]
                next_page_num = re.findall("\d+", next_pages)[0].strip()
                if next_page_num is not None:
                    next_page_url = "http://www.chinadrugtrials.org.cn/clinicaltrials.searchlist.dhtml?currentpage=" + next_page_num
                    yield scrapy.Request(next_page_url, cookies=self.home_page_cookie, callback=self.parse)
        elif response.status == 202:
            print("主页面 " + current_page + " 爬取失败，获取cookie重新进行爬取，url ----------------------------------- ", response.url)
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-automation'])
            # options.add_argument(('--proxy-server=' + self.proxy))
            browser = webdriver.Chrome(options=options)
            browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                                    Object.defineProperty(navigator, 'webdriver', {
                                      get: () => undefined
                                    })
                                  """
            })
            browser.get(response.url)
            cookies = {}
            for cookie in browser.get_cookies():
                cookies[cookie['name']] = cookie['value']
            self.home_page_cookie = cookies
            selector = fromstring(browser.page_source)
            browser.quit()
            homeContent = selector.xpath("//table[@class='searchTable']//tr[position()>1]")
            if len(homeContent) > 0:
                print("主页面 " + current_page + " 爬取成功，url ----------------------------------- ", response.url)
                # 获取主页数据
                for sel in homeContent:
                    item = DrugtrialsItem()
                    item['num'] = sel.xpath('normalize-space(./td[1]/text())')
                    item['reg_num'] = sel.xpath('normalize-space(./td[2]/a/text())')
                    item['status'] = sel.xpath('normalize-space(./td[3]/a/text())')
                    item['drug_name'] = sel.xpath('normalize-space(./td[4]/a/text())')
                    item['indications'] = sel.xpath('normalize-space(./td[5]/a/text())')
                    item['topic'] = sel.xpath('normalize-space(./td[6]/a/text())')
                    yield item
                    yield scrapy.Request(
                        "http://www.chinadrugtrials.org.cn/clinicaltrials.searchlistdetail.dhtml?currentpage=" +
                        str(item['num']).strip(), cookies=self.detail_page_cookie, callback=self.get_detail)
                # 自动获取下一页的url
                next_pages = selector.xpath('//ul[@class="pagination"]/li[last()]/a/@onclick')
                next_page_num = re.findall("\d+", str(next_pages))[0].strip()
                if next_page_num is not None:
                    next_page_url = "http://www.chinadrugtrials.org.cn/clinicaltrials.searchlist.dhtml?currentpage=" + next_page_num
                    yield scrapy.Request(next_page_url, cookies=self.home_page_cookie, callback=self.parse)
        elif response.status == 403:
            print("主页面 " + current_page + " 爬取失败，ip可能被封，url ----------------------------------- ", response.url)



    def get_detail(self, response):
        detailTable = []
        if response.status == 200:
            detailTable = response.xpath("//table[@class='searchDetailTable']")
            # get detail info
            if len(detailTable) > 0:
                print("详情页爬取success  ----------------------------------- " + response.url)
                item = DrugtrialsDetailItem()
                item['trial_id'] = response.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][1]//tr[1]/td/text())").extract()[
                    0]
                item['drug_name'] = response.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][1]//tr[3]/td/text())").extract()[
                    0]
                item['indications'] = response.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][1]//tr[6]/td/text())").extract()[
                    0]
                item['topic'] = response.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][1]//tr[8]/td/text())").extract()[
                    0]

                item['applicant'] = response.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][2]//tr[1]/td/div/input/@value)").extract()[
                    0]
                item['contact_name'] = response.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][2]//tr[2]/td[1]/text())").extract()[
                    0]
                item['contact_num'] = response.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][2]//tr[2]/td[2]/text())").extract()[
                    0]
                item['contact_phone'] = response.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][2]//tr[2]/td[3]/text())").extract()[
                    0]
                item['contact_email'] = response.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][2]//tr[3]/td[1]/text())").extract()[
                    0]
                item['contact_address'] = response.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][2]//tr[3]/td[2]/text())").extract()[
                    0]

                item['age'] = response.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][4]//tr[1]/td[1]/text())").extract()[
                    0]
                item['gender'] = response.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][4]//tr[2]/td[1]/text())").extract()[
                    0]
                inclusion_criteria = ""
                for obj in response.xpath(
                        "//div[@id='collapseTwo']//table[@class='searchDetailTable'][4]//tr[4]//table[@class='subSearch']//tr"):
                    inclusion_criteria += obj.xpath('normalize-space(./td[2]/text())').extract()[0] + "\n"
                item['inclusion_criteria'] = inclusion_criteria
                exclusion_criteria = ""
                for obj in response.xpath(
                        "//div[@id='collapseTwo']//table[@class='searchDetailTable'][4]//tr[5]//table[@class='subSearch']//tr"):
                    exclusion_criteria += obj.xpath('normalize-space(./td[2]/text())').extract()[0] + "\n"
                item['exclusion_criteria'] = exclusion_criteria
                yield item
        elif response.status == 202:
            print("详情页爬取失败，获取cookie重新进行爬取，url ----------------------------------- ", response.url)
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-automation'])
            # options.add_argument(('--proxy-server=' + self.proxy))
            browser = webdriver.Chrome(options=options)
            browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                        Object.defineProperty(navigator, 'webdriver', {
                          get: () => undefined
                        })
                      """
            })
            browser.get(response.url)
            cookies = {}
            for cookie in browser.get_cookies():
                cookies[cookie['name']] = cookie['value']
            self.detail_page_cookie = cookies
            selector = fromstring(browser.page_source)
            browser.quit()
            # get detail info
            detailTable = selector.xpath("//table[@class='searchDetailTable']")
            if len(detailTable) > 0:
                print("详情页爬取success  ----------------------------------- " + response.url)
                item = DrugtrialsDetailItem()
                item['trial_id'] = selector.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][1]//tr[1]/td/text())")
                item['drug_name'] = selector.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][1]//tr[3]/td/text())")
                item['indications'] = selector.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][1]//tr[6]/td/text())")
                item['topic'] = selector.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][1]//tr[8]/td/text())")
                item['applicant'] = selector.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][2]//tr[1]/td/div/input/@value)")
                item['contact_name'] = selector.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][2]//tr[2]/td[1]/text())")
                item['contact_num'] = selector.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][2]//tr[2]/td[2]/text())")
                item['contact_phone'] = selector.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][2]//tr[2]/td[3]/text())")
                item['contact_email'] = selector.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][2]//tr[3]/td[1]/text())")
                item['contact_address'] = selector.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][2]//tr[3]/td[2]/text())")
                item['age'] = selector.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][4]//tr[1]/td[1]/text())")
                item['gender'] = selector.xpath(
                    "normalize-space(//div[@id='collapseTwo']//table[@class='searchDetailTable'][4]//tr[2]/td[1]/text())")
                inclusion_criteria = ""
                for obj in selector.xpath(
                        "//div[@id='collapseTwo']//table[@class='searchDetailTable'][4]//tr[4]//table[@class='subSearch']//tr"):
                    inclusion_criteria += obj.xpath('normalize-space(./td[2]/text())') + "\n"
                item['inclusion_criteria'] = inclusion_criteria
                exclusion_criteria = ""
                for obj in selector.xpath(
                        "//div[@id='collapseTwo']//table[@class='searchDetailTable'][4]//tr[5]//table[@class='subSearch']//tr"):
                    exclusion_criteria += obj.xpath('normalize-space(./td[2]/text())') + "\n"
                item['exclusion_criteria'] = exclusion_criteria
                yield item
        elif response.status == 403:
            print("详情页爬取失败，ip可能被封，url ----------------------------------- ", response.url)




