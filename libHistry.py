
from str import *

# 所需删除的后缀
deletes = ["'s","'re","'ll","'m","'t"]
deletefiles = ["lib/finished.txt",
                "lib/mainLib.txt",
                "lib/notimportent/notWords.txt"]


def unEdIng(word):
    def addE(word):
        adde = readfile('lib/notimportent/ingNeede.txt')
        addes = adde.split()
        if word in addes:
            return(True)
        return False
    notchange = readfile('lib/notimportent/notChange.txt')
    notchanges = notchange.split()
    if word in notchanges:
        return word
    if word[-3:] == "ing":
        if addE(word):
            return (word[:-3] + "e")
        return word[:-3]
    elif word[-1:] == 's':
        return word[:-1]
    return word

def cleartext(str):
    '''
        [专用] 清理额外符号
    imput
        str str:    输入的字符串
    output
        str str:  祛除标点符号,'s/'re...的字符串
    '''
    # 删除组合 's 're
    def clear1(str):
        for i in deletes:
            str = str.replace(i,'')
        return str

    # 祛除标点符号
    def claer2(str):
        Ls = set(str)
        for i in Ls:
            if i.isspace() or checkstr(i):
                continue
            str = str.replace(i,"")
        return str
    
    # main
    str = clear1(str)
    str = claer2(str)
    return str

def clearDic(dic):
    '[专用] dic 删除 file里所有单词'
    def clearDici(dic,file):
        t = readfile(file)
        Ls = t.split()
        for i in Ls:
            if i in dic:
                del(dic[i])
        return dic
    for i in deletefiles:
        dic = clearDici(dic,i)
    return dic
    


def writeNumberDic(n,dic,file):

    # 长度保险
    l = len(dic)
    if l < n:
        n = l

    string = ""
    ni = 0
    
    
    for i in dic:
        if ni >= n:
            break
        ni +=1
        # str
        a = str(dic[i])     # 次数
        while len(a) < 6:       # 文本
            a += " "
        a = a + i + '\n'  # 写入
        string += a
    print(string)

