# -*- coding: utf-8 -*-
import MeCab
import re
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

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

"""
x = range(MaxValue+1)
"""

hist = defaultdict(int)
for n in freq.values():
    hist[n] += 1
# 縦軸：その頻度である単語の数
# 横軸：ある頻度

"""
y = list(hist.values())
"""
x, y = tuple(zip(*sorted(hist.items())))
plt.xlim(0, max(x))
plt.ylim(0, max(y))
"""
for a, b in zip(x, y):
    print(a, b)
print(len(x), len(y))
"""
for _ in plt.bar(x, y):
    print(_)
plt.show()
