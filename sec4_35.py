#-*- coding: utf-8 -*-
import MeCab
import re

neko = open("neko.txt.mecab", "r")

raw = []
dic = []
for line in neko:
    raw.append(re.sub("\t|\n",",",line).split(","))

for raw_list in raw:
    if not (raw_list[0] == "EOS" or re.match("[。、…「」]|\u3000", raw_list[0])):
        dic.append({"surface": raw_list[0], "base": raw_list[7], "pos": raw_list[1], "pos1": raw_list[2]})

rensetu = []
for i in range(len(dic)-1):
    if dic[i]["pos"] == "名詞" and dic[i+1]["pos"] == "名詞":
        rensetu.append(dic[i]["surface"] + dic[i+1]["surface"])
print(rensetu)
mlen = max(len(x) for x in rensetu)
print([s for s in rensetu if len(s) == mlen])

