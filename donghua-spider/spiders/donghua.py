import scrapy


class DonghuaSpider(scrapy.Spider):
    name = 'donghua'
    allowed_domains = ['api.bilibili.com']
    page_index = 1
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
                'score': i['score']
            }
            yield donghua
        self.page_index += 1
        if self.page_index <= 51:
            next_page_url = self.base_url.format(self.page_index)
            print(next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse)
