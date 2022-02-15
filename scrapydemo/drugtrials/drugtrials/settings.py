# Scrapy settings for drugtrials project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'drugtrials'

SPIDER_MODULES = ['drugtrials.spiders']
NEWSPIDER_MODULE = 'drugtrials.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'drugtrials (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }
DEFAULT_REQUEST_HEADERS = {
    "authority": "www.chinadrugtrials.org.cn",
    "method": "POST",
    "path": "/clinicaltrials.searchlist.dhtml",
    "scheme": "http",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate",
    "accept-language": "zh-CN,zh;q=0.9",
    "origin": "http://www.chinadrugtrials.org.cn",
    "referer": "http://www.chinadrugtrials.org.cn/index.html",
    "Cookie": "FSSBBIl1UgzbN7N80S=9WZOr7niYHF0G7fwLWlv7b7FwpZfxQV8ww4IWWgVEG0Jpef3ArSwsukUhoMDip4J; JSESSIONID=6676A018928E6A1AD2B1B6A3CB6C3133; token=tUi1CWNlk9DUibnWy1iCJal5R21sGuj24__JYozG3qU2z3zi2jb4a1zCiio; FSSBBIl1UgzbN7N80T=3DPUN4_Ppkqf1YJN2TIfkeekqQMKX6B9AB2W6sUQ50NmMJX014hS.HjddycgaId6qp1PWkAkxnaPh1JzoT.LQRcbaSH6kbVxNnOMk4bPtw00Y4pmFYCwKoeDg8kLAas_35KXs4OLIz0H3XfpE.dJyBCCjpnuWULUOXrtTGoUj0Kz4rVeuaKEclYQxqOPfhsWmpL2ZP88qBdyZ0KKE_iL.FTqf_LaEJWRDH_dD95hcLLxkhCO2Ym8ttFhg_rhsVLvWhu8CtoQuWL.TmbpZGGVT2Et.fZmf5MtLnZ1GguqWyvB05V5spKXau6IqOwdN.MIkgOw2tsGRmaprIaW4C5bKlXSGZbxK0f2sbm0h3AEXgqZY.q",
    "User-Agent": "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'drugtrials.middlewares.DrugtrialsSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'drugtrials.middlewares.DrugtrialsDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'drugtrials.pipelines.DrugtrialsPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 数据库地址
MYSQL_HOST = 'localhost'
# 数据库用户名:
MYSQL_USER = 'root'
# 数据库密码
MYSQL_PASSWORD = '1qaz@WSX3edc@rwebox.com'
# 数据库端口
MYSQL_PORT = 3306
# 数据库名称
MYSQL_DBNAME = 'chictr'
# 数据库编码
MYSQL_CHARSET = 'utf8'
