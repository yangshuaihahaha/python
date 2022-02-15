import requests
from selenium import webdriver
# list 页面操作
if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    options.add_argument("--proxy-server=http://221.182.31.54:8080")

    browser = webdriver.Chrome(options=options)
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
                            Object.defineProperty(navigator, 'webdriver', {
                              get: () => undefined
                            })
                          """
    })
    browser.get("http://www.chinadrugtrials.org.cn/clinicaltrials.searchlist.dhtml")

    print(browser.get_cookies())
    cookies = {}
    for cookie in browser.get_cookies():
        cookies[cookie['name']] = cookie['value']
    print(cookies)
    # browser.quit()
