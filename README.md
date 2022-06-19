# 1. CiCiHelper 终端命令助手
CiCiHelper是由wangzirui32开发的终端命令助手，可以查询命令的使用方式，具体参见下文，但目前项目仍处于测试状态，尚未添加更多命令。
# 2. 使用方式
1. 克隆此项目
2. 进入项目目录，安装依赖 `pip install -r requirements.txt`
3. 在项目文件夹的上一层，输入命令`python -m CiCiHelper.line_query query-desc --desc 目录`测试是否成功
# 3. 命令格式
1. 查询命令 `python -m CiCiHelper.line_query query-name --name [命令]`
2. 查询与关键词有关的命令 `python -m CiCiHelper.line_query query-desc --desc [关键词]`
# 4. 示例
输入命令：
```bash
python -m CiCiHelper.line_query query-name --name cd
```
输出：
```py
+----------+--------------+------------+
| 命令名称 |   命令说明   |  命令格式  |
+----------+--------------+------------+
|    cd    | 进入某个目录 | cd [-Path] |
+----------+--------------+------------+
```
***
输入命令：
```bash
python -m CiCiHelper.line_query query-desc --desc 目录
```
输出：
```py
+----------+--------------------------+---------------------------------------------------+
| 命令名称 |         命令说明         |                      命令格式                     |
+----------+--------------------------+---------------------------------------------------+
|    cd    |       进入某个目录       |                     cd [-Path]                    |
|  mkdir   |         创建目录         |                  mkdir [dirName]                  |
|   del    | 删除一个或数个文件或目录 | del [/P] [/F] [/S] [/Q] [/A[[:]attributes]] names |
+----------+--------------------------+---------------------------------------------------+
```
# 其它信息
CSDN：[https://blog.csdn.net/wangzirui32](https://blog.csdn.net/wangzirui32)

GitHub：[https://github.com/wangzirui32](https://github.com/wangzirui32)
***