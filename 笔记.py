# print是输出，input是输入，len是查询长度
print()
input(files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None)
len()
# str字符 int整型 float浮点型 
str(float)
int()
float()

# 语法
# if 判断 while 循环 for 循环
if condition:
    pass
elif expression:
    pass
else:
    pass


while expression:
    pass
else:
    pass


for i in range()
# 函数
# import声明函数库 sys.exit推出程序 def创建函数
import
sys.exit()
def funcname(parameter_list):
    pass

# 列表
# index查找 append insert插入 del remove删除 sort排序 list tuple转换 copy deepcopy 复制列表，需要声明 import copy
del 列表[i]
index(x)        .index查找
append(x)       .append
insert(i, x)    .insert插入
remove(x)       .remove删除
sort(sort_criteria, charset, search_criterion[, ...])   .sort排序
list([directory[, pattern]])),tuple()
copy.copy(x),copy.deepcopy(x)

# 字典
# key 键   values 内容   item 键+内容     get 获取，无则输出value    setdefault 获取，无则填写value
# ppint 漂亮打印
.key()  .values()   .item(index)
.get(key,value=None)    .setdefault(key, value=None)
pprint.pprint(object)   pprint.pformat(object)

# 字符串
# ''  ""  表示字符串 ''' ''' 表示输出同输入     """ """ 多行注释
# .upper(c) 大写  .lower(c) 小写    .isupper(c) 判断大写    .islower(c) 判断小写
# .isalpha(c) 只含字母  .isalnum(c) 只含数字字母  .isdecimal(c) 只含数字字符    .isspace(c) 只含空格、制表符、换行
# .istitle(c) 只含头字母大写后面小写的单词
# .startswith(c)  判断字符串开始   .endswith(c) 判断字符串结尾
# .join(path, *paths) 前面的加入到后面的列表并变成字符串 .split(path)    前面字符串的删除后面的并且分割成列表
# .ljust() 左对齐  .rjust() 右对齐    .center() 居中
# .strip() 删除   .lstrip() 删除左侧  .rstrip() 删除右侧
# pyperclip.copy() pyperclip.paste() 复制粘贴到剪贴板   import pyperclip
.upper(c)    .lower(c)    .isupper(c) .islower(c)
.isalpha(c) .isalnum(c) .isdecimal(c)   .isspace(c) .istitle(c)
.startswith(c)  .endswith(c)
.join(path, *paths) .split(path)
.ljust()    .rjust()    .center()
.strip()    .lstrip()   .rstrip()
pyperclip.copy()   pyperclip.paste()

# 正则表达式
# \d\d\d-\d\d\d-\d\d\d\d==\d{3}-\d{3}-\d{4}
# （\d\d\d）-(\d\d\d-\d\d\d\d)
# （\(\d\d\d\)）-(\d\d\d-\d\d\d\d)
# Batman|Tina Fey
# Bat(man|mobile|copter|bat)
# Bat(wo)?man   ? 零或一次
# Bat(wo)*man   * 零或多次
# Bat(wo)+man   * 一或多次
# .at   通配符 == cat hat sat
# *at   == flat
# .*    所有文本
# .DOTALL 所有字符  .I 不区分大小写   .VERBOSE 多行
# （HA）{3,5} 贪心  （HA）{3,5}？  非贪心
# .compile 判断标准 .search 用判断标准搜索一次   .findall 用判断标准判断多次  .sub 替换
# \d 0~9    \D 0~9以外的字符 \w 任何字母、数字或下划线  \W 除字母、数字和下划线以外的字符
# \s 空格、制表符或换行符 \S 除空格、制表符或换行符以外的字符
# [0-9] [a-z] [A-Z] [^abc](非）   ^（开头）   $(结尾)
.compile    .search .findall(string[, pos[, endpos]])   .sub(a, b)

# IO
# os.path.join() 寻址 import os