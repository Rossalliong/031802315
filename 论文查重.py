# coding: utf-8
import os

def readLines(filepath): #该函数用于读取路径为filepath的文本内容
    lines = []
    try:
        with open(filepath, 'r', encoding = 'utf-8') as f:
            lines = f.readlines() #读取文本所有行，结果保留在一个列表变量中
    except Exception:
        with open(filepath, 'r', encoding = 'gbk') as f:
            lines = f.readlines()
    return lines
    
def compare(file1, file2): #该函数用于比较两个文本的相似度
    lines1 = readLines(file1)
    lines2 = readLines(file2)
    
    count = 0.
    for line in lines1:
        if lines2.count(line) > 0: #用于统计字符串里某个字符出现的次数
            count += 1
    return count / max(len(lines1), len(lines2))
    
path = input() # 输入文本路径
dirs = os.listdir(path)
files = []
error_files = []
for file in dirs:
    files.append(os.path.join(path, file))

answer = input() #输入存放答案的文件路径

for i in range(1,len(files)):
    degree = compare(files[0], files[i]) #将每一个抄袭文本都与原文进行对比
    f = open(answer, mode = 'a',encoding='utf-8') #将答案输出到文件中
    print("开始查重",file=f)
    print("查重率：",file=f)
    print('%.2f'%degree,file=f)
    f.close()
            
