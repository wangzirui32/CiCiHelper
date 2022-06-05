from .cmd_db import CmdDatabase
from prettytable import PrettyTable

class ReadCmd():
    def show_cmds(cmds):
        show_table = PrettyTable(["命令名称", "命令说明", "命令格式"])
        for cmd in cmds:
            show_table.add_row([cmd.get("name"), cmd.get("desc"), cmd.get("format")])

        return show_table

    @staticmethod
    def query_cmd_name(name: str):
        """
        :param: name 命令名称
        :return: 命令详情
        """
        return CmdDatabase.read_cmd_by_name(name)

    @staticmethod
    def query_cmd_desc(desc):
        """
        :param: desc 命令描述字符串
        :return: 命令详情
        """
        return CmdDatabase.read_cmd_by_desc(desc)



if __name__ == '__main__':
    pass