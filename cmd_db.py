from tinydb import TinyDB, Query
import os

db = TinyDB(os.path.join(os.path.dirname(__file__), "cmd.json"))
cmd_table = db.table("cmd")
CMD = Query()

class CmdDatabase():
    @staticmethod
    def read_cmd_by_name(name: str):
        cmd = cmd_table.search(CMD.name==name.strip())

        return cmd

    @staticmethod
    def read_cmd_by_desc(desc: str):
        cmd = cmd_table.search(CMD.desc.search(desc.strip()))

        return cmd

    @staticmethod
    def insert_cmd(name: str, desc: str, cmd_format: str):
        if CmdDatabase.read_cmd_by_name(name): raise Exception("The command already exists.")
        cmd_table.insert({
            "name": name,
            "desc": desc,
            "format": cmd_format
        })

if __name__ == '__main__':
    pass
