import scrapy as scrapy
import datetime
import requests

class GlobalClinicalTrialSpider(scrapy.Spider):
    name = "globalclinicaltrialspider"
    allowed_domains = ["globalclinicaltrialdata.com"]

    start_time = datetime.datetime.strptime("2020-01-01", '%Y-%m-%d')
    next_time = None
    end_time = datetime.datetime.now()

    interval = 1
    start_urls = [
        "https://globalclinicaltrialdata.com"
    ]
    download_url = "https://globalclinicaltrialdata.com/download"

    def parse(self, response):
        if self.start_time < self.end_time:
            self.next_time = self.start_time + datetime.timedelta(days=+self.interval)
            if self.next_time > self.end_time:
                self.next_time = self.end_time
            received_from = self.start_time.strftime("%m/%d/%Y")
            received_to = self.next_time.strftime("%m/%d/%Y")
            self.start_time = self.next_time + datetime.timedelta(days=+1)
            meta = {
                "query": "",
                "recr": "Not yet Recruiting;Recruiting;Available;Completed;Terminated;Suspended;Withdrawn;Withheld;Active, not recruiting;Enrolling by invitation;Expanded Access: Temporarily not available;Expanded Access: No longer available;Expanded Access: Approved for marketing",
                "source": "US;EU;JP;CN;CN2;NZ",
                "phase": "Phase 0;Phase 1;Phase 2;Phase 3;Phase 4",
                "updated_from": "",
                "updated_to": "",
                "received_from": received_from,
                "received_to": received_to,
                "role": "Patient",
                "resources": ""
            }

            head = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
            }

            res = requests.post('https://globalclinicaltrialdata.com/download', headers=head, data=meta, verify=False)

            yield scrapy.Request(self.download_url, method="POST", meta=meta, callback=self.parse)
