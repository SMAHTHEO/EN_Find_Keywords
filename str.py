''' 文件操作 文本操作'''

def readfile(file):
    '读取文件'
    f = open(file)
    str = f.read()
    f.close()
    return str

def writefile(file, str):
    '写入文件'
    f = open(file, 'w')
    f.write(str)
    f.close

def sortfile(file):
    '排序文件'
    string = readfile(file)
    strings = string.split('\n')
    strings = sorted(strings)
    newstring = "\n".join(strings)
    writefile(file, newstring)


def checkstr(sti):
    '检测当前字符串是否全是字母'
    Ls = "abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ"
    for i in sti:
        if i not in Ls:
            return False
    return True
    
def numberList(List):
    '列表计数'
    dic = dict()
    for i in List:      # 计数
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    dic = sorted(dic.items(),key = lambda a:a[1])   #排序
    dic = dic[::-1]
    dic = dict(dic)
    return dic


if __name__ == "__main__":
    sortfile('lib/finished.txt')
    sortfile('lib/notimportent/notCHange.txt')