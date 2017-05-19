# -*- coding: utf-8 -*-

import json
import re

with open("jawiki-country.json") as f:
    lines = f.readlines()

datas = [json.loads(line) for line in lines]

uk = [country for country in datas if country["title"] == "イギリス"][0]

"""
print(uk["text"])


print("Categories:")
categories = re.findall(".*Category.*\n", uk["text"])
[print(w) for w in categories]
"""

print("Category names:")
category_names = re.findall("(.*Category:)([\w・]*)(.*)", uk["text"])
[print(w[1]) for w in category_names]
