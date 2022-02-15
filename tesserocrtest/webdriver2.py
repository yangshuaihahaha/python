from selenium import webdriver
from lxml.html import fromstring

def crawler():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(options=options)

    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
    })
    browser.get('http://www.chinadrugtrials.org.cn/clinicaltrials.searchlist.dhtml')
    selector = fromstring(browser.page_source)
    trContent = selector.xpath("//table[@class='searchTable']/tr[position()>1]")
    print(trContent)

if __name__ == "__main__":
    crawler()
