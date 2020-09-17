# This module is kept for backwards compatibility, so users can import
# scrapy.conf.settings and get the settings they expect
# 该模块为了向后兼容, 这样用户可以导入scrapy.conf.settings的值得到配置文件的值

import sys

# sys.modules 当前环境加载的模块
if 'scrapy.cmdline' not in sys.modules:
    # 
    from scrapy.utils.project import get_project_settings
    settings = get_project_settings()

import warnings
from scrapy.exceptions import ScrapyDeprecationWarning
warnings.warn("Module `scrapy.conf` is deprecated, use `crawler.settings` attribute instead",
    ScrapyDeprecationWarning, stacklevel=2)
