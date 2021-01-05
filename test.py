#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import re
import json

path = "./pos_lonyo63" #資料夾目錄

files= os.listdir(path) #得到資料夾下的所有檔名稱
s = []
for file in files: #遍歷資料夾
    if not os.path.isdir(file):#判斷是否是資料夾,不是資料夾才打開
        f = open(path+"/"+file, "r", encoding = "utf-8"); #開啟檔案
        iter_f = iter(f); #建立迭代器
        str = ""
        for line in iter_f: #遍歷檔案,一行行遍歷,讀取文字
            str =  line
            s.append(str) #每個檔案的文字存到list中   

print(s) #列印結果

#re提出名詞
resultLIST = []
pat = re.compile(r"((?<=<ENTITY_oov>)|(?<=<ENTITY_nounHead>)|(?<=<ENTITY_noun>)|(?<=<ENTITY_nouny>)).*?(?=<)")
for i in s:
    resultLIST.append([p.group(0) for p in pat.finditer(i)])
    
print(resultLIST)

filename = 'result.json'
finalresultLIST = []
resultDICT = {}

#利用詞頻分析將各篇名詞提出，使同篇同名詞不重複計算
for index in resultLIST:
    countlist = {}
    for i in index:
        if i in countlist:
            pass
        else:
            countlist[i] = index.count(i)
    print(countlist)
    for i in countlist:
        finalresultLIST.append(i)
print(finalresultLIST)

#詞頻分析不同篇之食材
for i in finalresultLIST:
    if i in resultDICT:
        pass
    else:
        resultDICT[i] = finalresultLIST.count(i)
        
print(resultDICT)
     
with open(filename, "w", encoding = "utf-8") as f:
    json.dump(resultDICT, f, ensure_ascii = False)

    
