# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .items import ChictrItem
from .items import ChictrDetailItem
from pymysql import cursors
from twisted.enterprise import adbapi
import logging
import copy


class ChictrPipeline:
    # 函数初始化
    def __init__(self, db_pool):
        self.db_pool = db_pool

    @classmethod  # 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
    def from_settings(cls, settings):
        """类方法，只加载一次，数据库初始化"""
        db_params = dict(
            host=settings['MYSQL_HOST'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            port=settings['MYSQL_PORT'],
            database=settings['MYSQL_DBNAME'],
            charset=settings['MYSQL_CHARSET'],
            use_unicode=True,
            # 设置游标类型
            cursorclass=cursors.DictCursor
        )
        # 创建连接池
        db_pool = adbapi.ConnectionPool('pymysql', **db_params)
        # 返回一个pipeline对象
        return cls(db_pool)

    def process_item(self, item, spider):
        """
        数据处理
        :param item:
        :param spider:
        :return:
        """
        myItem = {}
        if isinstance(item, ChictrItem):
            print("----------------------ChictrItem----------------------")
            myItem["page"] = item["page"]
            myItem["regSite"] = item["regSite"][0]
            myItem["href"] = item["href"][0]
            myItem["regNum"] = item["regNum"][0]
            myItem["regTop"] = item["regTop"][0]
            myItem["stuType"] = item["stuType"][0]
            myItem["regDate"] = item["regDate"][0]
            # 对象拷贝，深拷贝
            chictrItem = copy.deepcopy(myItem)
            # 把要执行的sql放入连接池
            query = self.db_pool.runInteraction(self.insert_into_chictr, chictrItem)
            # 如果sql执行发送错误,自动回调addErrBack()函数
            query.addErrback(self.handle_error, myItem, spider)
            return myItem
        elif isinstance(item, ChictrDetailItem):
            print("----------------------ChictrDetailItem----------------------")
            myItem['page'] = item['page']
            myItem['trial_id'] = item['trial_id'][0]
            myItem['reg_name'] = item['reg_name'][0]
            myItem['date_registration'] = item['date_registration'][0]
            myItem['study_type'] = item['study_type'][0]
            myItem['public_title'] = item['public_title'][0]
            myItem['contact_name'] = item['contact_name'][0]
            myItem['contact_address'] = item['contact_address'][0]
            myItem['contact_telephone'] = item['contact_telephone'][0]
            myItem['contact_email'] = item['contact_email'][0]
            myItem['inclusion_criteria'] = item['inclusion_criteria'][0]
            myItem['agemin'] = item['agemin'][0]
            myItem['agemax'] = item['agemax'][0]
            myItem['gender'] = item['gender'][0]
            myItem['exclusion_criteria'] = item['exclusion_criteria'][0]
            # 对象拷贝，深拷贝
            chictrDetailItem = copy.deepcopy(myItem)
            # 把要执行的sql放入连接池
            query = self.db_pool.runInteraction(self.insert_into_chictrdetail, chictrDetailItem)
            # 如果sql执行发送错误,自动回调addErrBack()函数
            query.addErrback(self.handle_error, myItem, spider)
            return myItem
        logging.info(myItem)

    # 处理sql函数
    def insert_into_chictr(self, cursor, item):
        print("-----------------", item)
        # 创建sql语句
        sql = "INSERT INTO chictr (page, reg_site, href, reg_num, reg_top, stu_type, reg_date) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(item["page"], item["regSite"], item["href"], item["regNum"], item["regTop"], item["stuType"], item["regDate"])
        # 执行sql语句
        print("sql-----------------", sql)
        cursor.execute(sql)

    # 处理sql函数
    def insert_into_chictrdetail(self, cursor, item):
        print("-----------------", item)
        # 创建sql语句
        sql = "INSERT INTO chictr_detail (page, trial_id, reg_name, date_registration, study_type, public_title, contact_name, contact_address, contact_telephone, contact_email, inclusion_criteria, agemin, agemax, gender, exclusion_criteria) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(item["page"], item["trial_id"], item["reg_name"], item["date_registration"], item["study_type"], item["public_title"],item["contact_name"],item["contact_address"], item["contact_telephone"], item["contact_email"], item["inclusion_criteria"], item["agemin"], item["agemax"],item["gender"],item["exclusion_criteria"])
        # 执行sql语句
        print("sql-----------------", sql)
        cursor.execute(sql)

    # 错误函数
    def handle_error(self, failure, item, spider):
        # #输出错误信息
        print("failure", failure)
