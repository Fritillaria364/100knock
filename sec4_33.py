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

for dic_line in dic:
    # print(dic_line)
    if dic_line["pos1"] == "サ変接続":
        print(dic_line)

