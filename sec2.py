# -*-coding: utf-8-*- #
import nltk, re, random
import sys

# Section 2

# 10
f = open("hightemp.txt")
raw = []
for line in f:
    raw.append(line.strip())
print(len(raw))

# 11
sents = [w.replace("\t", " ") for w in raw]
print(sents)
f.close()

# 12
col1 = open("col1.txt", "w")
col2 = open("col2.txt", "w")
for w in sents:
    col1.write(w[0] + "\n")
    col2.write(w[1] + "\n")
col1.close()
col2.close()

# 13
c1 = open("col1.txt", "r")
c2 = open("col2.txt", "r")
col3 = open("col3.txt", "w")
l1 = c1.readlines()
l2 = c2.readlines()
[col3.write("{0}\t{1}\n".format(l1[i].rstrip("\n"), l2[i].rstrip("\n"))) for i in range(len(l1))]

"""
# 14,15
args = sys.argv
print(sents[0:int(args[1])])
print(sents[-int(args[1]):])
"""

# 16
args = sys.argv
law = len(sents)/int(args[1])
for i in range(int(args[1])):
    splt = open("splt{0}.txt".format(i), "w")
    [splt.write(w+"\n") for w in sents[int(law*i):int(law*(i+1))]]

"""
law/n -> 行数
sents[0:law]
sents[law:law*2]
"""

# 17
head = set([w[0] for w in sents])

# 18
sentsList = [w.rsplit() for w in sents]
sort_sent = sorted(sentsList, key=lambda temp: float(temp[2]), reverse=True)
print(sort_sent)

# 19
fd = nltk.FreqDist([w[0] for w in sents])
fd.most_common()

