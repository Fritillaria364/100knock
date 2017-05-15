# -*-coding: utf-8-*- #
import nltk, re, random
import sys

# functions
def ngram(seq, n):
    gram = []
    for i in range(len(seq) - n+1):
        gram.append(tuple(w for w in seq[i:i + n]))
        # gram.append(tuple(seq[i:i + n])) - forの部分はいらない
    return gram

def templete(x,y,z):
    print("{0}時の{1}は{2}".format(x, y, z))
    # print(str(x) + "時の" + y + "は" +str(z))

def cipher(s):
    res = ""
    for w in s:
        if w.islower():
            res += chr(219-ord(w))
        else:
            res += w
    return res

def MyShuffle(s):
    ind = random.sample(s[1:-1],len(s)-2)
    return s[0] + "".join(ind) + s[-1]

# Section 1

"""
# 00.
str = "stressed"
print(str[::-1])
"""

"""
# 01.
str = "パタトクカシーー"
print(str[::2])
"""

"""
# 02.
str1 = "パトカー"
str2 = "タクシー"
for i, j in zip(str1, str2):
    print(i+j,end="")

・かっこいい
print("".join(i+j for i,j in zip(str1,str2) ) )
"""

"""
# 03.
raw = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
sent = re.findall(r'\w+', raw)
word_count = [len(w) for w in sent]
print(word_count)
"""

"""
# 04.
dic = {}
raw = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur " \
      "King Can. "
sent = re.findall(r'\w+', raw)
# 分割は
ind = [1, 5, 6, 7, 8, 9, 15, 16]
for i in range(len(sent)):
# enumerate - リストない要素とインデックスを両方取ってこれるすごいの
    if (i+1) in ind:
        dic[sent[i][:1]] = i
    else:
        dic[sent[i][:2]] = i
print(dic)
"""

"""
# 05.
raw = "I am an NLPer"
sent = re.findall(r'\w+', raw)

print(ngram(raw, 2))
print(ngram(sent, 2))
"""

"""
# 06.
X = set(ngram("paraparaparadise", 2))
Y = set(ngram("paragraph", 2))
Z = set(X | Y)
A = set(X ^ Y) # ^じゃなくて&
B = X - Y

print(X)
print(Y)
print(A)
"""

"""
# 08.
raw = "I need 100 healing!!!"
print(cipher(raw))
print(cipher(cipher(raw)))
"""

"""
# 09.
raw = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human " \
      "mind ."
# sent = re.findall(r"\w+",raw)
sent = re.split(r" ",raw)
res = []
for w in sent:
    if len(w)>4:
        res.append(MyShuffle(w))
    else:
        res.append(w)
print(" ".join(res))
"""


# リスト内包表記を使おう！！！！！！！！