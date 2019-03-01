# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors

class AhuiPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db='ahuife',  # 数据库名
            user='root',  # 数据库用户名
            passwd='123456',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            """insert into ygo(card_name_zn, card_name_ja,card_name_en,card_keys,card_origin,card_level,
            card_type,card_code,card_ak,card_dk
            )
            value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",  # 纯属python操作mysql知识，不熟悉请恶补
            (item['card_name_zn'],  # item里面定义的字段和表字段对应
             item['card_name_ja'],item['card_name_en'],item['card_keys'],item['card_origin'],item['card_level'],item['card_type'],
             item['card_code'],item['card_ak'],item['card_dk'],))
        # 提交sql语句
        self.connect.commit()
        return item  # 必须实现返回
