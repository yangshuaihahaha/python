from selenium import webdriver
import requests


def getCookies():
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
    browser.get('http://www.chinadrugtrials.org.cn/index.html')
    cookietext = ""
    for cookie in browser.get_cookies():
        cookietext += cookie['name'] + "=" + cookie['value'] + "; "
    browser.quit()
    return cookietext


def crawler():
    head = {
        "Cookie": getCookies(),
        "Referer": "http://www.chinadrugtrials.org.cn/index.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
    }
    url = 'http://www.chinadrugtrials.org.cn/clinicaltrials.searchlistdetail.dhtml'
    html = requests.get(url, headers=head).text
    print(html)


if __name__ == "__main__":
    crawler()
