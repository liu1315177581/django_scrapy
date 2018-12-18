import scrapy, re, datetime, json
from python_vedio.vedio import models
from scrapy_splash.request import SplashRequest, SplashFormRequest
class vedio(scrapy.Spider):
    '''视频网站爬虫'''
    name = 'vedio'


    def start_requests(self):
        '''
        爬虫入口函数
        :return: 调用主解析函数
        '''

        splash_args = {
            "lua_source": """
                            --splash.response_body_enabled = true
                            splash.private_mode_enabled = false
                            splash:set_user_agent("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")
                            assert(splash:go("http://www.k2938.com/type/1.html"))
                            splash:wait(3)
                            return {html = splash:html()}
                        """
        }
        yield SplashRequest("http://www.k2938.com/type/1.html", args=splash_args, callback=self.mainParse)



    def mainParse(self, response):
        '''
        主解析函数
        :param response: 爬取的链接对象
        :return:
        '''

        # 爬取内容
        style_find = response.css('div.col-sm-4')
        # 循环容器
        for i in style_find:
            content_url = i.css('.movie-item > a::attr(href)').extract_first()
            # 判断可以点进去的时候
            if content_url is not None:
                # 合并路由，形成爬取路径
                content_url = response.urljoin(content_url)
                # 传递路径，进行内容页爬取，调用contextParse函数
                str_url = """
                    --splash.response_body_enabled = true
                    splash.private_mode_enabled = false
                    splash:set_user_agent("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")
                    assert(splash:go(%s))
                    splash:wait(3)
                    return {html = splash:html()}
                """%(content_url)
                splash_args = {"lua_source": str_url}
                yield SplashRequest(content_url, args=splash_args, callback=self.contextParse)


        # 爬取下一页
        page_content = response.css('div.container > div:nth-of-type(3)')
        # 找到按钮上的文字，用来判断是否是最后一页
        weiye_text = page_content.css('a:last-of-type::text').extract_first()
        # 如果是尾页的时候，根据爬取页面进行逻辑操作
        if weiye_text == '尾页':
            if page_content.css('a::text').extract()[-2] == '下一页':
                next_url = page_content.css('a::attr(href)').extract()[-2]
                # 判断路径不为None时
                if next_url is not None:
                    # 合并成新的路径
                    next_url = response.urljoin(next_url)
                    # 回调自己进行深入爬取
                    str_url = """
                        --splash.response_body_enabled = true
                        splash.private_mode_enabled = false
                        splash:set_user_agent("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")
                        assert(splash:go(%s))
                        splash:wait(3)
                        return {html = splash:html()}
                    """ % (next_url)
                    splash_args = {"lua_source": str_url}
                    yield SplashRequest(next_url, args=splash_args, callback=self.parse)



    def contextParse(self, response):
        '''
        :message 内容页处理函数
        :param  response
        :return 调用解析播放url,第一步
        '''

        print(response)
        pass

    # start_urls = [
    #     # 'http://www.juduoba.com/type/2.html',
    #     # 'http://www.k2938.com/'
    #     # 电影
    #     # 'http://www.k2938.com/type/1.html',
    #     # 'http://www.d6080.com/list/1/1.html'
    # ]

    def parse(self, response):
        '''
        :param response: res对象
        :return: 深入爬取
        '''

        # 爬取容器
        style_find = response.css('div.col-sm-4')

        # 循环容器
        for i in style_find:
            # 爬取内容页
            content_url = i.css('.movie-item > a::attr(href)').extract_first()
            # 判断可以点进去的时候
            if content_url is not None:
                # 合并路由，形成爬取路径
                content_url = response.urljoin(content_url)
                # 传递路径，进行内容页爬取，调用context_parse函数
                yield scrapy.Request(content_url, callback=self.context_parse)

        # 判断有下一页的时候回调
        page_content = response.css('div.container > div:nth-of-type(3)')
        # 找到按钮上的文字，用来判断是否是最后一页
        weiye_text = page_content.css('a:last-of-type::text').extract_first()
        # 如果是尾页的时候，根据爬取页面进行逻辑操作
        if weiye_text == '尾页':
            if page_content.css('a::text').extract()[-2] == '下一页':
                next_url = page_content.css('a::attr(href)').extract()[-2]
                # 判断路径不为None时
                if next_url is not None:
                    # 合并成新的路径
                    next_url = response.urljoin(next_url)
                    # 回调自己进行深入爬取
                    yield scrapy.Request(next_url, callback=self.parse)





    def context_parse(self, response):
        '''
        :message 内容页处理函数
        :param  response
        :return 调用解析播放url,第一步
        '''

        # 爬取容器
        content = response.css('div.container')
        # 爬取资源名称
        resourcesName = content.css('h1.movie-title::text').extract_first(),
        # 资源orm
        resourcesItem = models.Resources(
            # 资源名称
            name = resourcesName,
            # 资源上线时间
            release_date = content.css('table.table-condensed tr:nth-child(6) td:nth-child(2)::text').extract_first()[0:10],
            # 语言类型
            language_type = '',
            # 资源介绍
            text_content = content.css('p.summary::text').extract_first(),
            # 资源产地
            place_origin = content.css('table.table-condensed tr:nth-child(4) td:nth-child(2)::text').extract_first(),
            # 资源横图
            row_url = content.css('img.img-thumbnail::attr(src)').extract_first(),
            # 资源纵图
            column_url = content.css('img.img-thumbnail::attr(src)').extract_first(),
            # 时间
            date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            # 资源链接
            url = ''
        )
        # 导演名称
        directorName = content.css('table.table-condensed tr:nth-child(1) td:nth-child(2)::text').extract_first()
        # 导演orm
        directorItem = models.Director(
            # 导演名称
            name = directorName,
        )


        # 爬取播放链接
        res_li = content.css('.dslist-group .dslist-group-item')
        # 循环链接
        for i in res_li:
            # 获取链接
            res_url = i.css('a::attr(href)').extract_first()
            # 集数|或者语言类型
            resourcesItem.episode = i.css('a::text').extract_first()
            # 判断链接不为None
            if res_url is not None:
                # 合并形成新的链接
                res_url = response.urljoin(res_url)
                # 传递路径，调用url_parse_own函数，进行爬取链接
                yield scrapy.Request(
                    res_url,
                    callback=self.url_parse_own,
                    meta={
                        'resourcesItem': resourcesItem,
                        'directorItem': directorItem,
                        'directorName': directorName,
                        'resourcesName': resourcesName
                    }
                )





    def url_parse_own(self, response):
        '''
        :message 解析资源url,第一步
        :param  response对象
        :return 调用解析播放url,第二步
        '''

        # 爬取资源链接
        res_url = response.css('.player iframe::attr(src)').extract_first()
        # 判断不为None
        if res_url is not None:
            # 传递路径，调用url_parse_two函数，进行爬取链接
            yield scrapy.Request(res_url, callback=self.url_parse_two, meta=response.meta)


    def url_parse_two(self, response):
        '''
        :message 解析播放url,第二步
        :param  response:
        :return 返回item
        '''
        resourcesItem = response.meta['resourcesItem']
        directorItem = response.meta['directorItem']

        # 正则匹配资源链接
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        print(response)
        return
        content = response.view()
        if content is not None:
            resourcesItem.url = re.findall(pattern, content)[1]


        # 根据条件获取导演名字
        getItemDirectorName = models.Director.objects.filter(name=response.meta['directorName'])
        # 声明一个导演ormId
        directorId = None
        # 判断没有的时候，进行新增
        if len(getItemDirectorName) <= 0:
            # 存库
            directorItem.save()
            # 变量赋值（新增的id）
            directorId = directorItem.id
        else:
            # 变量赋值（获取库中的id）
            directorId = getItemDirectorName[0].id
        # 根据条件获取资源名称
        getResourcesName = models.Resources.objects.filter(name=response.meta['resourcesName'])
        # 判断没有的时候，进行新增
        if len(getResourcesName) <= 0:
            # 存库
            resourcesItem.save()
        # 判断有的时候，进行获取
        else:
            # 获取库中的数据
            resourcesItem = getResourcesName[0]
        # 设置关联关系
        resourcesItem.director_name.set([directorId])

