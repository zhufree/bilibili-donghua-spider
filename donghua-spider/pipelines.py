# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json, xlwt

class DonghuaPipeline:
    def open_spider(self, spider):
        # json file
        # self.file = open('{}-items.json'.format(spider.name), 'w', encoding='utf-8')
        # excel file
        self.workbook = xlwt.Workbook(encoding='ascii')
        self.worksheet = self.workbook.add_sheet("Sheet1")
        self.worksheet.write(0,0, "标题")
        self.worksheet.write(0,1, "简介")
        self.worksheet.write(0,2, "链接")
        self.worksheet.write(0,3, "评分")
        self.row = 1

    def process_item(self, item, spider):
        # json file
        # line = json.dumps(item, ensure_ascii=False) + "\n"
        # self.file.write(line)
        # excel file
        self.worksheet.write(self.row, 0, item['title'])
        self.worksheet.write(self.row, 1, item['subTitle'])
        self.worksheet.write(self.row, 2, item['link'])
        self.worksheet.write(self.row, 3, item['score'])
        self.row += 1
        return item

    def close_spider(self, spider):
        # json file
        # self.file.close()
        # excel file
        self.workbook.save('{}-items.xls'.format(spider.name))
    