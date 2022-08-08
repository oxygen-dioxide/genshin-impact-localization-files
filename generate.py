#从全语言字典json生成中英markdown
import json
import unidecode

fulldict=json.load(open("dict.json",encoding="utf8"))
#zh>en
dictlist=[(x,"## "+x.upper()) for x in "abcdefghijklmnopqrstuvwxyz"]
for (pagename,worddict) in fulldict.items():
    if("zhs" in worddict and "zhs_rm" in worddict):#汉字和拼音都有
        if("en" in worddict):
            english=worddict["en"]
        else:#如果没有英文，则用页面名称
            english=pagename.split("#")[0]
        #print(pagename)
        dictlist.append((unidecode.unidecode(worddict["zhs_rm"]).lower(),"- **{}** {}".format(worddict["zhs"],english)))
dictlist.sort(key=(lambda x:x[0]))
open("zh_en.md","w",encoding="utf8").write("# 原神汉英词典\n# Genshin Impact Chinese-English Dictionary\n收录游戏《原神》中，官方名词的中文及英文翻译\n\n内容来自[Genshin Impact Wiki](https://genshin-impact.fandom.com/)，在CC-BY-SA协议下提供。\n\n可使用Ctrl+F在本页面查找。\n\n"+"\n".join([x[-1] for x in dictlist]))