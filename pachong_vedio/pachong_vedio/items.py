# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from python_vedio.vedio.models import Resources
from python_vedio.vedio.models import Tag
from python_vedio.vedio.models import Type
from python_vedio.vedio.models import Director
from python_vedio.vedio.models import Actor



class PachongVedioResources(DjangoItem):
    '''
    资源表
    '''
    # define the fields for your item here like:
    django_model = Resources

class PachongVedioTag(DjangoItem):
    '''
    电影类型表（惊险，搞笑...）
    '''
    django_model = Tag

class PachongVedioType(DjangoItem):
    '''
    类型（电视剧，电影，小视频）
    '''
    django_model = Type

class PachongVedioDirector(DjangoItem):
    '''
    导演表
    '''
    django_model = Director

class PachongVedioActor(DjangoItem):
    '''
    演员表
    '''
    django_model = Actor




    # res 标识资源表
    # res_name = scrapy.Field()           # 资源名称
    # res_release_date = scrapy.Field()   # 资源上线时间
    # res_url = scrapy.Field()            # 资源url
    # res_text_content = scrapy.Field()   # 资源描述
    # res_place_origin = scrapy.Field()   # 产地
    # res_row_url = scrapy.Field()        # 横图
    # res_column_url = scrapy.Field()     # 纵图
    # res_episode = scrapy.Field()        # 集数（电视剧）|备选（电影）
    #
    # # tag 标识类型表
    # tag_name = scrapy.Field()           # 类型名称
    #
    #
    # # type 标识视频种类表
    # type_name = scrapy.Field()          # 种类名称
    #
    #
    # # dire 标识导演表
    # dire_name = scrapy.Field()          # 名称
    # dire_sex = scrapy.Field()           # 性别
    # dire_country = scrapy.Field()       # 国籍
    # dire_date_birth = scrapy.Field()    # 出生年月
    # dire_base_city = scrapy.Field()     # 籍贯省
    # dire_nation = scrapy.Field()        # 民族
    #
    #
    # # actor 标识演员表
    # actor_name = scrapy.Field()          # 名称
    # actor_sex = scrapy.Field()           # 性别
    # actor_country = scrapy.Field()       # 国籍
    # actor_date_birth = scrapy.Field()    # 出生年月
    # actor_base_city = scrapy.Field()     # 籍贯省
    # actor_nation = scrapy.Field()        # 民族
    #
    # # vResTag 标识（资源与标签）关联表
    # vResTag_resources_id = scrapy.Field()           # 资源id
    # vResTag_tag_id = scrapy.Field()                 # 标签id
    #
    # # vResType 标识（资源与类型）关联表
    # vResType_resources_id = scrapy.Field()          # 资源id
    # vResType_type_id = scrapy.Field()               # 类型id
    #
    # # vResActorName 标识（资源与演员）关联表
    # vResActorName_resources_id = scrapy.Field()     # 资源id
    # vResActorName_actor_id = scrapy.Field()         # 演员id
    #
    # # vResDireName 标识（资源与导演）关联表
    # vResDireName_resources_id = scrapy.Field()      # 资源id
    # vResDireName_director_id = scrapy.Field()       # 导演id
    # pass


