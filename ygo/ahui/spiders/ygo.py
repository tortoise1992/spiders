#coding:utf-8
# 解决https网站的反扒问题
from twisted.internet.ssl import AcceptableCiphers
from scrapy.core.downloader import contextfactory
import scrapy
from ahui.items import AhuiItem
contextfactory.DEFAULT_CIPHERS = AcceptableCiphers.fromOpenSSLCipherString('DEFAULT:!DH')

class ygo(scrapy.Spider):
    name = 'ygo'
    allowed_domains = ["www.ygo-sem.cn"]
    # 随机取一个开始的页面，然后通过下一页去获取其他的页面
    start_urls = [
        'https://www.ygo-sem.cn/html/7/6/21251800.html'
    ]
    def parse(self, response):
        item = AhuiItem()  # 实例化item类
        # 解析所需要的数据
        card_img=response.css('#card_frame #card_image_1::attr(src)').extract_first()
        card_info=response.css('.item_box')
        card_list=[item.css('.item_box_value::text').extract_first().strip() for item in card_info]
        # 按照位置，0是中文名，1是日文名，2是英文名，3是属性，4是种族，5是星级，6是怪兽类型，7是卡片code，8是攻击力，9是守备力
        print(card_list)
        if len(card_list) == 10 :
            item['card_name_zn']=card_list[0]
            item['card_name_ja'] = card_list[1]
            item['card_name_en'] = card_list[2]
            item['card_keys'] = card_list[3]
            item['card_origin'] = card_list[4]
            item['card_level'] = card_list[5]
            item['card_type'] = card_list[6]
            item['card_code'] = card_list[7]
            item['card_ak'] = card_list[8]
            item['card_dk'] = card_list[9]
            yield item
        else:
            pass
        # 检查是否存在下一页
        next_page=response.css('#Apre')
        if next_page is not None:
            next_page=response.css('#Apre::attr(href)').extract_first()
            next_page=response.urljoin(next_page)
            print(next_page)
            yield scrapy.Request(url=next_page,callback=self.parse,dont_filter=True)





