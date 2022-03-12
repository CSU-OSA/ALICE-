import re

# 只需要修改这两个文件就行
source_mht = 'chat_info.mht'
target_txt = 'target.txt'

# 文件打开并按行读取
f = open(source_mht, mode='r+', encoding='UTF-8')
data = f.readlines()
new_data = ''
# 筛选聊天记录中的有效文本
for i in data:
    inside = re.findall('<tr><td><div.*color=\'000000\'>(.+?)</font></div></td></tr>', i)
    if inside:  # 不为空则加入data中
        new_data = new_data + str(inside) + '\n'
# 将筛选得到的new_data放回文件中
# 不知道为什么不塞回去就不能进行对聊天记录的简单筛选
# 挺奇怪的
# w+是复写模式
f = open(target_txt, mode='w+', encoding='UTF-8')
f.writelines(new_data)
f.close()
# 打开文本
f = f = open(target_txt, mode='r+', encoding='UTF-8')
data = f.readlines()
new_data = ''
# 对文本中一些常见的无效字符进行替换
for i in data:
    i = re.sub('&nbsp;', '', i)
    i = re.sub('\\[\'', '', i)
    i = re.sub('\'\\]', '', i)
    i = re.sub('<br>', '\n', i)
    new_data = new_data + i + '\n'
# 放回target_txt
f = open(target_txt, mode='w+', encoding='UTF-8')
f.writelines(new_data)
f.close()
