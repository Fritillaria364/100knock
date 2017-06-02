#-*- coding: utf-8 -*-
import requests
import json
import re

with open("jawiki-country.json") as f:
    lines = f.readlines()

datas = [json.loads(line) for line in lines]

uk = [country for country in datas if country["title"] == "イギリス"][0]

print(uk["text"])

baseinfo = re.findall("\{\{基礎情報(.*)^\}\}$", uk["text"], re.DOTALL | re.M)
BaseDic = {item: re.sub(r"(<.*>)|([\[\]])+|([\"\']+)", "", about) for item, about in re.findall("([\w /-]+) = (.+)", baseinfo[0])}


API_URL = "http://en.wikipedia.org/w/api.php?action=query&titles=Files:"
prp = "&prop=imageinfo&format=json"
# prp = "&prop=imageinfo&iiprop=url&format=json"

req = requests.get(API_URL + BaseDic["国旗画像"] + prp)

flag_json = json.loads(req.text)
# flag_json["query"]["pages"]["23473560"]["imageinfo"][0]["url"]
