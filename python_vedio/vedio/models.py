from django.db import models
import datetime
# Create your models here.


class Resources(models.Model):
    '''资源表（电影资源表）'''
    name = models.CharField(max_length=255)                          # 资源名称
    director_name = models.ManyToManyField('Director')             # 导演名称
    release_date = models.DateTimeField()                            # 资源的上映时间
    type = models.ManyToManyField('Type')                           # 资源类型
    language_type = models.CharField(max_length=255, null=True)     # 语言类型
    url = models.CharField(max_length=255)                           # 资源url
    actor_name = models.ManyToManyField('Actor')                    # 演员名称
    tag = models.ManyToManyField('Tag')                             # 资源的类型标签
    text_content = models.TextField(null=True)                      # 资源文本描述
    place_origin = models.CharField(max_length=255, null=True)      # 产地
    row_url = models.CharField(max_length=255, null=True)           # 横图
    column_url = models.CharField(max_length=255,null=True)         # 纵图
    date_time = models.DateTimeField(auto_now=True)                 # 时间
    episode = models.CharField(max_length=100, null=True)                         # 集数或者备选

class Tag(models.Model):
    '''电影类型表（惊险，搞笑）'''
    name = models.CharField(max_length=255, unique=True)            # 资源的标签名称
    date_time = models.DateTimeField(auto_now=True)                 # 时间

class Type(models.Model):
    '''类型（电视剧，电影，小视频）'''
    name = models.CharField(max_length=255, unique=True)            # 类型名称
    text = models.CharField(max_length=20, unique=True, default=None)# 类型名称（汉字）
    date_time = models.DateTimeField(auto_now=True)                 # 时间

class Director(models.Model):
    '''导演表'''
    name = models.CharField(max_length=255)                         # 人员名称
    sex = models.CharField(max_length=1, null=True)                 # 性别
    country = models.CharField(max_length=10, null=True)            # 国家
    nation = models.CharField(max_length=5, null=True)              # 民族
    base_city = models.CharField(max_length=10, null=True)          # 省
    date_birth = models.CharField(max_length=255, null=True)        # 出生年月
    date_time = models.DateTimeField(auto_now=True)                 # 时间
    text_content = models.TextField(null=True)                      # 导演文本描述


class Actor(models.Model):
    '''演员表'''
    name = models.CharField(max_length=255)                         # 人员名称
    sex = models.CharField(max_length=1, null=True)                 # 性别
    country = models.CharField(max_length=10, null=True)            # 国家
    nation = models.CharField(max_length=5, null=True)              # 民族
    base_city = models.CharField(max_length=10, null=True)          # 省
    date_birth = models.CharField(max_length=255, null=True)        # 出生年月
    date_time = models.DateTimeField(auto_now=True)                 # 时间
    text_content = models.TextField(null=True)                      # 演员文本描述









