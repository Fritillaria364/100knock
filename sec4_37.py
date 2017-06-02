# -*- coding: utf-8 -*-
import MeCab
import re
import matplotlib.pyplot as plt
import numpy as np
import re

neko = open("neko.txt.mecab", "r")

raw = []
dic = []
for line in neko:
    raw.append(re.sub("\t|\n", ",", line).split(","))

for raw_list in raw:
    if not (raw_list[0] == "EOS" or re.match("[。、…「」]|\u3000", raw_list[0])):
        dic.append({"surface": raw_list[0], "base": raw_list[7], "pos": raw_list[1], "pos1": raw_list[2]})

freq = {}
for s in dic:
    freq[s["surface"]] = freq.get(s["surface"], 0) + 1


freq10Within = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]

x = range(1, 11)
y = [s[1] for s in freq10Within]
plt.bar(x, y)
plt.show()
