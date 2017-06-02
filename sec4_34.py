#-*- coding: utf-8 -*-
import MeCab
import re

neko = open("neko.txt.mecab", "r")

raw = []
dic = []
for line in neko:
    raw.append(re.sub("\t|\n",",",line).split(","))

for raw_list in raw:
    # print(raw_list)
    if not raw_list[0] == "EOS" and not re.match("[。、…「」]|\u3000", raw_list[0]):
        dic.append({"surface": raw_list[0], "base": raw_list[7], "pos": raw_list[1], "pos1": raw_list[2]})

for i in range(1, len(dic)-1):
    if dic[i-1]["pos"]=="名詞" and dic[i]["surface"] == "の" and dic[i+1]["pos"] == "名詞":
        print(dic[i-1]["surface"] + "の" + dic[i+1]["surface"])


