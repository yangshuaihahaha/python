# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymysql import cursors
from twisted.enterprise import adbapi
import logging
from .items import DrugtrialsItem
from .items import DrugtrialsDetailItem
import copy
import pymysql

class DrugtrialsPipeline:
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
        if isinstance(item, DrugtrialsItem):
            print("----------------------DrugtrialsItem----------------------")
            myItem["num"] = int(item["num"].strip())
            myItem["reg_num"] = item["reg_num"]
            myItem["status"] = item["status"]
            myItem["drug_name"] = item["drug_name"]
            myItem["indications"] = item["indications"]
            myItem["topic"] = item["topic"]
            # 对象拷贝，深拷贝
            drugtrialsItem = copy.deepcopy(myItem)
            # 把要执行的sql放入连接池
            query = self.db_pool.runInteraction(self.insert_into_drugtrials, drugtrialsItem)
            # 如果sql执行发送错误,自动回调addErrBack()函数
            query.addErrback(self.handle_error, myItem, spider)
            return myItem
        elif isinstance(item, DrugtrialsDetailItem):
            print("----------------------DrugtrialsDetailItem----------------------")
            myItem["trial_id"] = item["trial_id"]
            myItem["drug_name"] = item["drug_name"]
            myItem["indications"] = item["indications"]
            myItem["topic"] = item["topic"]
            myItem["applicant"] = item["applicant"]
            myItem["contact_name"] = item["contact_name"]
            myItem["contact_num"] = item["contact_num"]
            myItem["contact_phone"] = item["contact_phone"]
            myItem["contact_email"] = item["contact_email"]
            myItem["contact_address"] = item["contact_address"]
            myItem["age"] = item["age"]
            myItem["gender"] = item["gender"]
            myItem["inclusion_criteria"] = item["inclusion_criteria"]
            myItem["exclusion_criteria"] = item["exclusion_criteria"]
            # 对象拷贝，深拷贝
            drugtrialsDetailItem = copy.deepcopy(myItem)
            # 把要执行的sql放入连接池
            query = self.db_pool.runInteraction(self.insert_into_drugtrials_detail, drugtrialsDetailItem)
            # 如果sql执行发送错误,自动回调addErrBack()函数
            query.addErrback(self.handle_error, myItem, spider)
            return myItem
        logging.info(myItem)

    # 处理sql函数
    def insert_into_drugtrials(self, cursor, item):
        # 创建sql语句
        sql = "INSERT INTO drugtrials (num, reg_num, status, drug_name, indications, topic) VALUES ('{}','{}','{}','{}','{}','{}')".format(
            item["num"], pymysql.escape_string(item["reg_num"]), pymysql.escape_string(item["status"]), pymysql.escape_string(item["drug_name"]), pymysql.escape_string(item["indications"]), pymysql.escape_string(item["topic"]))
        # 执行sql语句
        print("sql-----------------", sql)
        cursor.execute(sql)

    def insert_into_drugtrials_detail(self, cursor, item):
        # 创建sql语句
        sql = "INSERT INTO drugtrials_detail (trial_id, drug_name, indications, topic, applicant, contact_name, contact_num, contact_phone, contact_email, contact_address, age, gender, inclusion_criteria, exclusion_criteria) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"\
            .format(pymysql.escape_string(item["trial_id"]), pymysql.escape_string(item["drug_name"]), pymysql.escape_string(item["indications"]), pymysql.escape_string(item["topic"]), pymysql.escape_string(item["applicant"]), pymysql.escape_string(item["contact_name"]), pymysql.escape_string(item["contact_num"]), pymysql.escape_string(item["contact_phone"]), pymysql.escape_string(item["contact_email"]), pymysql.escape_string(item["contact_address"]), pymysql.escape_string(item["age"]), pymysql.escape_string(item["gender"]), pymysql.escape_string(item["inclusion_criteria"]), pymysql.escape_string(item["exclusion_criteria"]))
        # 执行sql语句
        sql = sql.replace("'","\"")
        print("sql-----------------", sql)
        cursor.execute(sql)

    # 错误函数
    def handle_error(self, failure, item, spider):
        # #输出错误信息
        print("failure", failure)
