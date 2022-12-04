

from str import *
from libHistry import *

'读取'
text = readfile("now.txt") 
'清理符号'
text = cleartext(text)
'列表'
words = text.split()
'小写'
for i in range(len(words)):
    words[i] = words[i].lower()
    words[i] = unEdIng(words[i])
'计数'
numberWords = numberList(words)
'查重'
numberWords = clearDic(numberWords)
print(numberWords)
writeNumberDic(50,numberWords,"")


