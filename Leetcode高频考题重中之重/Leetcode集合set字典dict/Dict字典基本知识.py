# 字典的定义 {key1: value1, key2:value2...}
print(type({1:1, 2:2, 3:3}))  # 查询类型
# 输出：<class 'dict'>
{'Q':'新月打击', 'W':'苍白之瀑', 'E':'月之降临', 'R':'月神冲刺'}
print({'Q':'新月打击', 'W':'苍白之瀑', 'E':'月之降临', 'R':'月神冲刺'}['Q'])
# 输出：新月打击
print({'Q':'新月打击', 'W':'苍白之瀑', 'E':'月之降临', 'R':'月神冲刺'}['W'])
print({'Q':'新月打击', 'W':'苍白之瀑', 'E':'月之降临', 'R':'月神冲刺'}['E'])
print({'Q':'新月打击', 'W':'苍白之瀑', 'E':'月之降临', 'R':'月神冲刺'}['R'])

print({'Q':'新月打击', 'Q':'苍白之瀑', 'E':'月之降临', 'R':'月神冲刺'}['Q'])  # 字典中不允许出现同名的键
print({1:'新月打击', '1':'苍白之瀑', 'E':'月之降临', 'R':'月神冲刺'})  # 字典的键既可以是数字也可以是字符串
# {1: '新月打击', '1': '苍白之瀑', 'E': '月之降临', 'R': '月神冲刺'}

#  注意：
#  1.key是不可变的类型，不允许用列表[]
#  2.value可以是str, int, float等等
print(type({}))