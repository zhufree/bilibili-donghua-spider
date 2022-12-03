import scrapy


class DonghuaSpider(scrapy.Spider):
    # name = 'fanju'
    name = 'donghua'
    allowed_domains = ['api.bilibili.com']
    page_index = 1
    # type = 1 番剧
    # type = 4 国创
    start_urls = ['https://api.bilibili.com/pgc/season/index/result?order=3&st=4&sort=0&page=1&season_type=4&pagesize=20&type=1']
    base_url = 'https://api.bilibili.com/pgc/season/index/result?order=3&st=4&sort=0&page={}&season_type=4&pagesize=20&type=1'
    
    def parse(self, response):
        res_json = response.json()
        data_list = res_json['data']['list']
        for i in data_list:
            donghua = {
                'title': i['title'],
                'subTitle': i['subTitle'],
                'link': i['link'],
                'score': i['score'],
                'season_id': i['season_id'],
                'media_id': i['media_id']
            }
            yield scrapy.Request(f'https://api.bilibili.com/pgc/web/season/stat?season_id={donghua["season_id"]}', callback=self.parse_detail, cb_kwargs=dict(data=donghua))
        # next page
        self.page_index += 1
        if len(data_list) == 20:
            next_page_url = self.base_url.format(self.page_index)
            print(next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_detail(self, response, data):
        res_json = response.json()
        result = res_json['result']
        data.update(result)
        yield data