# -*- coding: utf-8 -*-

import json
import re

with open("jawiki-country.json") as f:
    lines = f.readlines()

datas = [json.loads(line) for line in lines]

uk = [country for country in datas if country["title"] == "イギリス"][0]


print(uk["text"])

"""
print("Categories:")
categories = re.findall(".*Category.*\n", uk["text"])
[print(w) for w in categories]


print("Category Names:")
category_names = [w[1] for w in re.findall("(.*Category:)([\w・]*)(.*)", uk["text"])]
[print(w) for w in category_names]
"""

"""
print("Section Name:")
section_list = re.findall("(=+)(\w+)(=+)", uk["text"])
section_dic = {name : len(level)-1 for level, name, tmp in section_list}
print(section_dic)
"""

"""
print("Media File:")
media_list = [w[1] for w in re.findall("(ファイル:)(.+\.\w+)", uk["text"])]
print(media_list)
"""

"""
print("Extract Template:")
base_info = re.findall("\{\{基礎情報(.*)^\}\}$", uk["text"], re.DOTALL | re.M)
base_dic = {item: about for item, about in re.findall("([\w /-]+) = (.+)", baseinfo[0])}
"""

{item: re.sub(r"[\"\']+", "", about) for item, about in re.findall("([\w /-]+) = (.+)", baseinfo[0])}
{item: re.sub(r"([\[\]])+|([\"\']+)", "", about) for item, about in re.findall("([\w /-]+) = (.+)", baseinfo[0])}
{item: re.sub(r"(<.*>)|([\[\]])+|([\"\']+)", "", about) for item, about in re.findall("([\w /-]+) = (.+)", baseinfo[0])}

