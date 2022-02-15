import requests
import os

proxy = {
    'http': 'http://113.214.13.1:1080'
}
head = {
    "Cookie": "FSSBBIl1UgzbN7N80S=.b7yUMzKJVt5L2dpdv3MaTW_wQ4phUWVA_jo0fUTEVimUTOi.Fbk5ySq19NkTUf1; token=XKws1sTjfjZlzVcgrpFRGpiXAl_fwEUakOPpTl9SPcMuRpSSH2zHZoRZ9Nc; JSESSIONID=46FD6F81557B9FBF8BACE3C3939479AB; FSSBBIl1UgzbN7N80T=3p99arczpTnvoWi6kXG3WYFaWSajXdarn_zFJYn2LJqaFXWnX8UPqCp5MPte_oAx2y.5yY91i5C2z.qN4pe8pTi9fR.wxVLcqFqF4eWP_SNOy5Zxo6XLkUplcrapV5CjSI_fQSY9lpP9a0vowov.sZR4uzLJWnMK56D_JuvrDqWp2Go820JTNxFpekqI1BIztl4ZuOaxILjshdJXokpLTYpiWT2rRnkOSdkQo5MQRhCguvZYYAqI2YEFPHSALE03juD5fr0vBwMGzwnhCwkR1B_CE6LqrRHrK9FBQrxa1_iuyhBfFuMMqqLXTpBx7MXf.gRegaHB3oaVfkIQm5qL04Wv.l1vaVxCNH46g2OPI68TyCA",
    "Referer": "http://www.chinadrugtrials.org.cn/index.html",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}
filepath = os.path.join(os.curdir, "试验公示和查询.xls")
resp = requests.post("http://www.chinadrugtrials.org.cn/clinicaltrials.searchlist.dhtml?_export=xls&currentpage=1&secondLevel=1&sort=desc&sort2=desc&rule=CTR", headers=head, proxies=proxy)
print("status_code: " + str(resp.status_code))
print("text: " + resp.text)
# with open(filepath, "wb") as f:
#     for chunk in resp.iter_content(1024):
#         f.write(chunk)
