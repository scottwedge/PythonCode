# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihu.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhihu.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


HEADER={
    "Host": "www.zhihu.com",
    "Connection": "keep-alive",
    "Cache-Control": "no-store",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Referer": "https://www.zhihu.com/topic",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2",
}

COOKIES={
    'd_c0': r'"AIAAKffCNwqPTr6pJ1HwvHCaAUxT7n3z0zM=|1468320788"', 
    '_za': r'85e90fd6-cf8a-4ef3-89a9-73415791ca9e', 
    '_zap': r'ca943f37-321a-46e9-9863-7274f31ec869', 
    '_xsrf': r'3f26a6814b083dbfb84a67aff15ec8cc', 
    'q_c1': r'ce90cca97d974e03bdf4f2af0cfed710|1469500004000|1469500004000', 
    '__utma': r'51854390.241231743.1469500160.1469500160.1469500160.1', 
    '__utmb': r'51854390.8.10.1469500160', 
    '__utmc': r'51854390', 
    '__utmz': r'51854390.1469500160.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/', 
    '__utmv': r'51854390.000--|2=registration_date=20140812=1^3=entry_date=20160726=1', 
    'a_t': r'"2.0AADAgN40AAAXAAAAwl2-VwAAwIDeNAAAAIAAKffCNwoXAAAAYQJVTcJdvlcASpTY-V1PhasuxBykxP8UGn-mKJfk3UA1-4fhpO4tI7MP6ccmchRLWQ=="', 
    'z_c0': r'Mi4wQUFEQWdONDBBQUFBZ0FBcDk4STNDaGNBQUFCaEFsVk53bDItVndCS2xOajVYVS1GcXk3RUhLVEVfeFFhZjZZb2x3|1469501634|830f114ca52789e1af435b5fb5cecdcef54bf09b', 
    'cap_id': r'"NjgwOTRhZTZmMjUyNDM4ZjgxYmVjYmQzOWYxMzhjNjU=|1469501634|21dffd02472c0b64ce62de24510ef7ea132a5dcb"', 
    'l_cap_id': r'"Zjk0ZTQ4ZjhiM2Y3NDk1MmEzYTMwOWE2YzZjMGYwMjY=|1469501634|023c8cf9c52322ee9ee5c7d69b1b16956f2ebfcd"', 
    'login': r'"OGFjOWIyNzRkYWZlNDVkNjk3NjVmZGQ2YjE0ZjIzZTE=|1469501634|ccfc3c88ccf7501c18360cd50c259a8d2e8b9287"', 
    'n_c': r'1'
}
