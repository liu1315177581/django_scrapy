import scrapy, re
from pachong_vedio.items import PachongVedioResources, PachongVedioTag

class vedio(scrapy.Spider):
    '''视频网站爬虫'''
    name = 'vedio'
    start_urls = [
        'http://www.juduoba.com/type/2.html'
    ]

    def parse(self, response):
        itemResources = PachongVedioResources()
        itemTag = PachongVedioTag()



        itemResources['name'] = '天下无贼'
        itemTag['name'] = '动作片'
        print(itemTag)
        # yield itemResources
        # yield itemTag
        # style_find = response.css('div.col-sm-4')
        #
        # # 循环资源列表
        # for i in style_find:
        #     # 爬取内容页
        #     content_url = i.css('.movie-item > a::attr(href)').extract_first()
        #     if content_url is not None:
        #         content_url = response.urljoin(content_url)
        #         yield scrapy.Request(content_url, callback=self.context_parse)
        #
        # # 判断有下一页的时候回调
        # page_content = response.css('div.container > div:nth-of-type(3)')
        # weiye_text = page_content.css('a:last-of-type::text').extract_first()
        # if weiye_text == '尾页':
        #     if page_content.css('a::text').extract()[-2] == '下一页':
        #         next_url = page_content.css('a::attr(href)').extract()[-2]
        #         if next_url is not None:
        #             next_url = response.urljoin(next_url)
        #             yield scrapy.Request(next_url, callback=self.parse)





    def context_parse(self, response):
        '''
        :message 内容页处理函数
        :param  response
        :return 调用解析播放url,第一步
        '''

        # 生命item实例，进行赋值
        item = PachongVedioItem()
        content = response.css('div.container')

        # 名称
        item['res_name'] = content.css('h1.movie-title::text').extract_first()
        # 上线时间
        item['res_release_date'] = content.css('table.table-condensed tr:nth-child(6) td:nth-child(2)::text').extract_first()[0:10]
        # 资源介绍
        item['res_text_content'] = content.css('p.summary::text').extract_first()
        # 产地
        item['res_place_origin'] = content.css('table.table-condensed tr:nth-child(4) td:nth-child(2)::text').extract_first()
        # 纵图
        item['res_column_url'] = content.css('img.img-thumbnail::attr(src)').extract_first()
        # 导演
        item['dire_name'] = content.css('table.table-condensed tr:nth-child(1) td:nth-child(2)::text').extract_first()
        # 演员
        # item['']




        # 爬取播放链接
        res_li = content.css('.dslist-group .dslist-group-item')

        for i in res_li:
            res_url = i.css('a::attr(href)').extract_first()
            # 集数|或者语言类型
            item['res_episode'] = i.css('a::text').extract_first()
            if res_url is not None:
                res_url = response.urljoin(res_url)
                yield scrapy.Request(res_url, callback=self.url_parse_own, meta={'data': item})





    def url_parse_own(self, response):
        '''
        :message 解析资源url,第一步
        :param  response对象
        :return 调用解析播放url,第二步
        '''

        item = response.meta['data']
        res_url = response.css('.player iframe::attr(src)').extract_first()
        if res_url is not None:
            yield scrapy.Request(res_url, callback=self.url_parse_two, meta={'data': item})


    def url_parse_two(self, response):
        '''
        :message 解析播放url,第二步
        :param  response:
        :return 返回item
        '''

        # 取item值进行准备赋值
        item = response.meta['data']
        # 正则匹配资源链接
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        content = response.css('script::text').extract_first()
        item['res_url'] = re.findall(pattern, content)[0]
        yield item

