import os
import py7zr
import escape
import pathlib
import xmltodict

#解压缩
print("解压缩")
with py7zr.SevenZipFile('source/gensinimpact_pages_current.xml.7z', mode='r') as z:
    z.extractall()

#读xml文件
print("读xml文件")
xmlcontent=xmltodict.parse('<?xml version="1.0" encoding="utf-8"?>\n'+open("gensinimpact_pages_current.xml","r",encoding="utf8").read())
pages=xmlcontent["mediawiki"]["page"]
print("共有页面{}个".format(len(pages)))

#写入文件
pathlib.Path("pages").mkdir(exist_ok=True)
valid_page_number=0
for page in pages:
    #try:
        title=page["title"]
        if(not(":" in title)):#主命名空间
            valid_page_number+=1
            pagecode=page["revision"]["text"]["#text"]
            #写文件
            with open(os.path.join(".\\pages",escape.escape(title)+".wiki"),"w",encoding="utf8") as pagefile:
                pagefile.write(pagecode)
    #except:
    #    import ipdb
    #    ipdb.set_trace()
print("有效页面{}个".format(valid_page_number))