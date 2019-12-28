import os
import platform
import sys
from threading import Thread



class MyBasePyScripy(Thread):

    def __init__(self,  **payload):
        Thread.__init__(self)

        self.state = payload.get("state", "pass")



    def run(self):
        self.do_init() # 初始化
        self.do_test()


    def do_test(self):
        """
        执行单元
        :return: None
        """

        print("基类的do_test")

        return None

    def do_init(self):
        """
        基类自定义初始化
        :return:
        """
        self.sys_version = platform.uname().system  # 系统版本 Darwin Linux
        self.set_path() # 设置路径
        return None

    def set(self, command):

        return os.system(command)

    def set_command(self, command="pwd"):
        """
        设置命令 - 单条
        :param command: 命令
        :return: ret
        """

        return self.set(command)

    def set_path(self):
        """
        获取项目路径
        :return: None
        """

        self.project_path = os.path.abspath('.') # script 绝对路径
        self.uwsgi_path = self.project_path + "/app_sh/uwsgi" # uwsgi绝对路径
        self.nginx_path = self.project_path + "/app_sh/nginx" # nginx绝对路径

        return None

    def kill_pid(self, pid_list):
        """

        :param pid_list: 进程pid列表
        :return: None
        """
        if isinstance(pid_list,list):
            for foo in pid_list:
                print("kill -9 {}".format(foo))
                self.set_command("kill -9 {}".format(foo))
        else:
            pass

        return None


    def get_uwsgi_pid(self):
        """
        获取uwsgi进程的id
        :return: list
        """

        ret_list = []
        out = os.popen("ps -ef | grep uwsgi").read()
        for line in out.splitlines():
            ret_list.append(line.split()[1])

        print("uwsgi的所有进程: ",ret_list)

        return ret_list

    def get_nginx_pid(self):
        """
        获取nginx进程的id
        :return: list
        """

        ret_list = []
        out = os.popen("ps -ef | grep nginx").read()
        for line in out.splitlines():
            ret_list.append(line.split()[1])

        print("nginx的所有进程: ",ret_list)

        return ret_list
