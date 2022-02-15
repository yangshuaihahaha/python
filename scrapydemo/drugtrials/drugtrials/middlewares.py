# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from scrapy import signals
import requests
from fake_useragent import UserAgent
# useful for handling different item types with a single interface

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def get_available_proxy():
    available_proxy = None
    retry_count = 100
    while retry_count > 0:
        proxy = get_proxy().get("proxy")
        html = requests.get('http://www.chinadrugtrials.org.cn/index.html', proxies={"http": "http://{}".format(proxy)}, timeout=5)
        if html.status_code == 200:
            available_proxy = proxy
            break
        retry_count -= 1

    if retry_count < 1:
        print("重试了100次也没有得到可用的IP ----------------------------------- ")
        return None
    else:
        return available_proxy

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


class DrugtrialsSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DrugtrialsDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # return None
        # proxy = "http://" + get_available_proxy()
        # proxy = 'http://211.137.52.158:8080'
        # print("proxy ----------------------------------- " + proxy)
        # request.meta["proxy"] = proxy
        ua = UserAgent()
        request.headers['user-agent'] = ua.random
        request.headers['Cookie'] = "FSSBBIl1UgzbN7N80S=zyuLPZgQK8KaskIsP.87S340nATE0NTZNXoPCOh8nLNDYPrJq.MnXhbxfBK4wJtg; token=amQmE9gzzVKl55rOgrsoWpb1vp8FKTP0--WoKGa1xOQOTii8l23T4EyA7rN; FSSBBIl1UgzbN7N80T=3A8st9FPruJh3lpPgUk_x38fzTyBP8vZAONu6Ycv8du6JzrfVXckVILHD1fVdXOeMWJom.hV2d3FgUMOSWVRzAKMVLw66qdvFZEu9K_26hryc3SYXUDtDaYVQWceIYptY70noU6Uoy_Bd5MzygcpRoRwBh7yOQWX.r.QUpEK6WHMKVZgR2nsxpp4SmPDQTG7XTxNROMEWyq9gdZWLLW.CqOmu9ZzFrsYZX9eOloDHl1OJG6kHP7YOLiIf.VbJhHVxGO1h.7AIqf0LQ6E0JBkSrIEk_CSyq8aQ4mesnbCdQtNqhmN8d1z4l81Fd2mz.X_GI0g"

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
