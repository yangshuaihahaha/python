import requests

# list 页面操作
proxy = {
    'http': 'http://113.214.13.1:1080'
}
# head 信息
head = {
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Origin": "http://www.chinadrugtrials.org.cn",
    "Referer": "http://www.chinadrugtrials.org.cn/clinicaltrials.searchlist.dhtml",
    "Cookie": "FSSBBIl1UgzbN7N80S=.b7yUMzKJVt5L2dpdv3MaTW_wQ4phUWVA_jo0fUTEVimUTOi.Fbk5ySq19NkTUf1; JSESSIONID=46FD6F81557B9FBF8BACE3C3939479AB; token=eneA8R60D_Rn10xPMSrLSvsSDPDs_IZCTIqyB3SXuckf7hAZH7DzUvXHtyd; FSSBBIl1UgzbN7N80T=3ZBCl7xd23yTufm26k.tggpPgQ4gF14sDUbEygy6QGhPXkoGFuQa0MF7BHrBijMMpVG7JgBq_se6RDh4HZCW23mCYiAkG_UWbcq4tdDZqlvDvYCSIl6x6hAIWwLxrB.1IMA7SI2W.EKVOTMeJBeH0sBTudK8I6uSbE.yZq0NCTNybuHw8gpVZrc4OeiCvCSEpXeDDc9JJGcjTjVd7_7GU8szCO2rt35QheAZik2oiU3xVwy225G6ssBfMPD6o.fv1Kw5EluANbHquMyw6aJiWfNYfGWpNNGox.vzfvOGgOGS.Z030dVGW3lK3aGVP8620yIQk0x2PjnMC7c82uv8Z..h604g2B_Rc7e9vgL4NDhx4.G",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}
res = requests.post('http://www.chinadrugtrials.org.cn/clinicaltrials.searchlistdetail.dhtml?id=3ebce5b6a4d84f2f9570906cdac4f7ff&ckm_index=1&sort=desc&sort2=desc&rule=CTR&secondLevel=0&currentpage=1', proxies=proxy, headers=head)
print(res.status_code)
print(res.text)