# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors
import datetime

class PachongVedioPipeline(object):
    # def __init__(self):
    #     self.connect = pymysql.connect(
    #         host='127.0.0.1',  # 数据库地址
    #         port=3306,  # 数据库端口
    #         db='python_vedio',  # 数据库名
    #         user='root',  # 数据库用户名
    #         passwd='1234qwer',  # 数据库密码
    #         charset='utf8',  # 编码方式
    #         use_unicode=True
    #     )
    #     self.cursor = self.connect.cursor()

    def process_item(self, item, scrapy):
        item.save()
        return item
        # vedio_resources_sql = """
        #         INSERT INTO vedio_resources(
        #             name, release_date, url, text_content, place_origin, column_url, episode, date_time
        #         )
        #         SELECT %s, %s, %s, %s, %s, %s, %s, %s FROM DUAL
        #         WHERE NOT EXISTS(
        #             SELECT * FROM vedio_resources WHERE name=%s and release_date=%s and episode=%s
        #         )
        #     """,(
        #         item['res_name'],
        #         item['res_release_date'],
        #         item['res_url'],
        #         item['res_text_content'],
        #         item['res_place_origin'],
        #         item['res_column_url'],
        #         item['res_episode'],
        #         datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        #
        #         item['res_name'],
        #         item['res_release_date'],
        #         item['res_episode']
        #      )
        #
        # self.cursor.execute(vedio_resources_sql)
        # self.connect.commit()
        #
        # return item
