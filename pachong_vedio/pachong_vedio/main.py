import os, sys, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python_vedio.python_vedio.settings")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()
from scrapy import cmdline
cmdline.execute('scrapy crawl vedio'.split(' '))