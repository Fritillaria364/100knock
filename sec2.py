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


# 14,15
args = sys.argv
print(sents[0:int(args[1])])
print(sents[-int(args[1]):])

# 17
head = [w[0] for w in sents]

# 18


# 19
fd = nltk.FreqDist([w[0] for w in sents])
fd.most_common()

