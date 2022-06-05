from cmd_db import CmdDatabase

rules = [
    ("cd", "进入某个目录", "cd [-Path]"),
    ("mkdir", "创建目录", "mkdir [dirName]"),
    ("ipconfig", "查看ip设置", "ipconfig"),
    ("ping", "访问某个ip", "ping[-t] [-a] [-n count] [-l size] [-f] [-i TTL] [-v TOS][-r count] [-s count] [[-j host-list] | [-k host-list]][-w timeout] [-R] [-S srcaddr] [-c compartment] [-p][-4] [-6] target_name"),
    ("del", "删除一个或数个文件或目录", "del [/P] [/F] [/S] [/Q] [/A[[:]attributes]] names")
]

for i in rules:
    try: CmdDatabase.insert_cmd(i[0], i[1], i[2])
    except: continue