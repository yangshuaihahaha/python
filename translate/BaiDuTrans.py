# /usr/bin/env python
# coding=utf8

import httplib
import md5
import sys
import urllib
import random
import time
import json
reload(sys)
sys.setdefaultencoding( "utf-8" )

def query(q, fromLang='', toLang=''):
    if q:

        appid = '20201221000652730'  # 你的appid
        secretKey = '9XSrTCfHdUrnEEKmeym7'  # 你的密钥

        httpClient = None
        myurl = '/api/trans/vip/translate'
        salt = random.randint(32768, 65536)

        sign = appid + q + str(salt) + secretKey
        m1 = md5.new()
        m1.update(sign)
        sign = m1.hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.quote(
            str(q)) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign

        try:
            httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            res_result = json.loads(response.read())
            print '翻译成功 --------------------------- '
            return res_result['trans_result'][0]['dst']
        except Exception as e:
            print e
            print 'error_code: ' + res_result.get('error_code')
            if res_result.get('error_code') == u'54003':
                time.sleep(1)
                return query(q, fromLang, toLang)
        finally:
            if httpClient:
                httpClient.close()



if __name__ == '__main__':
    query('你在哪', 'zh', 'en')
