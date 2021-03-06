from .base import MyBasePyScript
import pymysql
import platform
import os
import sys
import requests



SQL_DATA = {
    "Darwin":{
        "db_data":{
            "ip":"127.0.0.1",
            "user":"root",
            "password":"root",
            "db_name":"blog_db",
        }
    },
    "Linux":{
        "db_data":{
            "ip":"127.0.0.1",
            "user":"root",
            "password":"root",
            "db_name":"blog_db",
        }
    },
    "Windows":{
        "db_data":{
            "ip":"127.0.0.1",
            "user":"root",
            "password":"root",
            "db_name":"blog_db",
        }
    }
}


class MyBaseSqlPyScript(MyBasePyScript):


    def __init__(self, **payload):
        MyBasePyScript.__init__(self, **payload)

    def run(self):

        self.do_init()
        self.do_test()
        self.do_exit()

    def do_init(self):

        self.get_sql_data() # 根据系统的不同, 设置不同的属性
        self.set_sql_path() # 配置路径, 基本的路径已经在基类的__init__设置过了

        return None

    def set_sql_path(self):

        self.sql_files_path = self.script_path + "/sql"  # .sql文件 绝对路径

        return None

    def get_sql_data(self):
        """
        根据系统的不同, 设置不同的属性
        :return: None
        """

        self.sql_ip = SQL_DATA.get(self.sys_version).get("db_data")["ip"]
        self.sql_user = SQL_DATA.get(self.sys_version).get("db_data")["user"]
        self.sql_password = SQL_DATA.get(self.sys_version).get("db_data")["password"]
        self.sql_db_name = SQL_DATA.get(self.sys_version).get("db_data")["db_name"]

        return None

    def del_db_migrations_files(self):
        """
        删除数据库迁移文件
        :return: None
        """

        for maindir, subdir, file_name_list in os.walk(self.project_path):
            if "migrations" in maindir and "__pycache__" not in maindir:
                for filename in file_name_list:
                    if "__init__.py" != filename:
                        initial_path = os.path.join(maindir, filename)  # 合并成一个完整路径
                        os.remove(initial_path) # 删除
        self.output_msg("数据库","迁移文件已删除")

        return None

    def create_db_models(self):
        """
        生成数据库模型
        :return: None
        """

        self.set_command_group(["{} {}manage.py makemigrations".format(self.python_evn, self.project_path)], "makemigrations")
        self.set_command_group(["{} {}manage.py migrate".format(self.python_evn, self.project_path)], "migrate")

        self.output_msg("数据库","Models已生成")

        return None

    def connect_db(self):
        """
        链接数据库
        :return: None
        """

        self.db_connect = pymysql.connect(
            host=self.sql_ip,
            user=self.sql_user,
            passwd=self.sql_password,
            charset="utf8",
        )
        self.output_msg("链接数据库","OK")

        self.db_cursor = self.db_connect.cursor() # 获取游标

        return None

    def crete_db(self):
        """
        操作数据库
        :return: None
        """

        self.output_msg("删除数据库", self.sql_db_name)
        self.execute_db_cmd("drop database {}".format(self.sql_db_name))  # 删除数据库

        self.output_msg("创建数据库", self.sql_db_name)
        self.execute_db_cmd("create database {} character set utf8".format(self.sql_db_name))  # 创建数据库

        return None

    def execute_db_cmd(self, cmd="show databases"):
        """
        执行数据库命令
        :param cmd: 命令
        :return: 返回执行结果
        """

        self.output_cmd("Sql命令> {};".format(cmd))

        return self.db_cursor.execute(cmd + ";")

    def close_db(self):
        """
        关闭链接
        :return: None
        """

        self.db_cursor.close()
        self.output_msg("关闭光标完成")

        self.db_connect.commit()
        self.output_msg("提交数据库")

        self.db_connect.close()
        self.output_msg("关闭连接完成")

        return None

    def copy_sql_files(self):
        """
        拷贝.sql到数据库
        :return: None
        """

        sql_file_abspath = self.get_sql_file_path_list(dir_path=self.sql_files_path, file_name="app_article_article.sql")
        self.set_command_group(["mysql -u {} -p{} -D{}  < {}".format(
            self.sql_user,
            self.sql_password,
            self.sql_db_name,
            sql_file_abspath
        )]) # 拷贝sql文件

        return None

    def get_sql_file_path_list(self, dir_path, file_name=""):
        """
        获取.sql文件的绝对路径
        :param dir_path: 文件夹路径
        :return:
        """

        for maindir, subdir, file_name_list in os.walk(dir_path):

            for filename in file_name_list:
                if file_name == filename:
                    return os.path.join(maindir, filename)  # 合并成一个完整路径
        return None

    def init_db(self):
        """
        初始化数据库
        :return: None
        """

        self.connect_db()  # 链接数据库
        self.crete_db()  # 操作数据库

        return None