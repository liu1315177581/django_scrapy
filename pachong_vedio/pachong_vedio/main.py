# 引入os,sys,django 模块
import os, sys, django

# 设置系统变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python_vedio.python_vedio.settings")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

# 引入命令模块
from scrapy import cmdline

# 执行爬虫命令
cmdline.execute('scrapy crawl vedio'.split(' '))