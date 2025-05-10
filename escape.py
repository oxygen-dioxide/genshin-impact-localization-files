#利用井号不能出现在mediawiki页面名称的特性来转义字符串
escapedict={
    "?":"#q",
    "\\":"#b",
    "/":"#s",
    '"':"#o",
    "*":"#a",
}

def escape(inputstring:str)->str:
    #字符串转文件名
    for (key,value) in escapedict.items():
        inputstring=inputstring.replace(key,value)
    return inputstring
    pass

def unescape(filename:str)->str:
    #文件名转字符串
    for (key,value) in escapedict.items():
        filename=filename.replace(value,key)
    return filename
    pass
