#提取wikitext中的other languages模板
import json
import escape
import pathlib
import wikitextparser

fulldict=dict()
for filepath in pathlib.Path(".\\pages").iterdir():
    pagename=escape.unescape(filepath.name[:-5])#删除后缀名，并解析转义，以获得页面名
    number=0
    content=wikitextparser.parse(filepath.read_text(encoding="utf8"))
    for template in content.templates:
        if(template.name.lower().strip(" \n") == "other languages"):
            worddict=dict()
            for argument in template.arguments:
                worddict[argument.name.strip(" \n")]=argument.value.strip(" \n")
            fulldict[pagename+"#"+str(number)]=worddict
            number+=1

print("localized words "+str(len(fulldict)))
print("output")
with open("dict.json","w",encoding="utf8") as outputfile:
    json.dump(fulldict,outputfile,ensure_ascii=False,indent=1)