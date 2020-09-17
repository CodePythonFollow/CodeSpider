"""
This modules implements the CrawlSpider which is the recommended spider to use
for scraping typical web sites that requires crawling pages.

See documentation in docs/topics/spiders.rst
"""

import copy
import six

from scrapy.http import Request, HtmlResponse
from scrapy.utils.spider import iterate_spider_output
from scrapy.spiders import Spider


def identity(x):
    return x

# 
class Rule(object):

    def __init__(self, link_extractor, callback=None, cb_kwargs=None, follow=None, process_links=None, process_request=identity):
        # 定义的提取链接规则
		self.link_extractor = link_extractor
		# 回调函数
        self.callback = callback
        self.cb_kwargs = cb_kwargs or {}
        self.process_links = process_links
        self.process_request = process_request
		# follow 指定了根据该规则从response提取的链接是否需要跟进
		# 如果callback为None，follow 默认设置为True，否则默认为False。 
        if follow is None:
            self.follow = False if callback else True
        else:
            self.follow = follow
		'''当follow为True时，爬虫会从获取的response中取出符合规则的url，再次进行爬取，
		如果这次爬取的response中还存在符合规则的url，则再次爬取，无限循环，直到不存在符合规则的url。'''

		
# 继承自Spider  
class CrawlSpider(Spider):
	
	# 是Rule对象的集合，用于匹配目标网站并排除干扰 
    rules = ()

    def __init__(self, *a, **kw):
        super(CrawlSpider, self).__init__(*a, **kw)
        self._compile_rules()
	
	# parse函数用在这里了，用来解析响应 所以在写crawlspider的时候不能写parse方法
    def parse(self, response):
        return self._parse_response(response, self.parse_start_url, cb_kwargs={}, follow=True)

    def parse_start_url(self, response):
        return []

    def process_results(self, response, results):
        return results

    def _build_request(self, rule, link):
		# 发出请求
        r = Request(url=link.url, callback=self._response_downloaded)
        r.meta.update(rule=rule, link_text=link.text)
        return r

    def _requests_to_follow(self, response):
        if not isinstance(response, HtmlResponse):
            return
        seen = set()
        for n, rule in enumerate(self._rules):
			# 提取出的链接最终交给_build_request方法重新发送
            links = [lnk for lnk in rule.link_extractor.extract_links(response)
                     if lnk not in seen]
            if links and rule.process_links:
                links = rule.process_links(links)
            for link in links:
                seen.add(link)
                r = self._build_request(n, link)
                yield rule.process_request(r)

    def _response_downloaded(self, response):
        rule = self._rules[response.meta['rule']]
        return self._parse_response(response, rule.callback, rule.cb_kwargs, rule.follow)
	
	# 解析响应
    def _parse_response(self, response, callback, cb_kwargs, follow=True):
	# 如果传入了callback，使用这个callback解析页面并获取解析得到的request或item
		# 如果有回调函数
        if callback:
            cb_res = callback(response, **cb_kwargs) or ()
            cb_res = self.process_results(response, cb_res)
            for requests_or_item in iterate_spider_output(cb_res):
                yield requests_or_item
		# 是否继续跟踪请求里面的网址
		# 判断有无follow，用_requests_to_follow解析响应是否有符合要求的link。
        if follow and self._follow_links:
			# _requests_to_follow又会获取link_extractor
            for request_or_item in self._requests_to_follow(response):
                yield request_or_item
				
	# CrawlSpider类会在init方法中调用_compile_rules方法，
	# 然后在其中浅拷贝rules中的各个Rule获取要用于回调(callback), 
	# 要进行处理的链接（process_links）和要进行的处理请求（process_request)
    def _compile_rules(self):
        def get_method(method):
            if callable(method):
                return method
            elif isinstance(method, six.string_types):
                return getattr(self, method, None)
		# 对rules里面的每个规则进行依次处理
        self._rules = [copy.copy(r) for r in self.rules]
        for rule in self._rules:
            rule.callback = get_method(rule.callback)
            rule.process_links = get_method(rule.process_links)
            rule.process_request = get_method(rule.process_request)

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(CrawlSpider, cls).from_crawler(crawler, *args, **kwargs)
        spider._follow_links = crawler.settings.getbool(
            'CRAWLSPIDER_FOLLOW_LINKS', True)
        return spider

    def set_crawler(self, crawler):
        super(CrawlSpider, self).set_crawler(crawler)
        self._follow_links = crawler.settings.getbool('CRAWLSPIDER_FOLLOW_LINKS', True)
