import re
import json
import os
import html


def get_dicts():
    thaire = re.compile('<td .*?class=th>(.*?)</td>',flags=re.DOTALL)
    engre = re.compile('<td .*? class=pos>.*?</td><td>(.*?)</td></tr>',flags=re.DOTALL)
    files = os.listdir('./thai_pages')
    thaieng = {}
    engthai = {}
    for filename in files:
        f = open('./thai_pages/'+filename,'r',encoding='utf-8')
        text = f.read()
        entries = get_table(text)
        
        for entry in entries:
            thai = re.findall(thaire,entry)[0]
            eng = re.findall(engre,entry)[0]
            
            thai = clean_text(thai)
            eng = clean_text(eng)
            
            thaieng[thai] = eng
            
            if eng in engthai:
                engthai[eng].append(thai)
            else:
                engthai[eng] = [thai]
                
    write_json('thai-eng.json',thaieng)
    write_json('eng-thai.json',engthai)

            
def clean_text(text):
    text = re.sub('<.*?>','',text)
    text = text.replace('&#34;','')
    text = text.replace('\n','; ')
    text = html.unescape(text)
    return text


def get_table(text):
    table = re.findall("<table width='100%' class=gridtable cellpadding='0' cellspacing='0'>(.*?)</table>",
                       text, flags=re.DOTALL)[0]
    entries = re.findall('<tr><td .*?class=th>.*?</td></tr>',
                         table, flags=re.DOTALL)
    return entries


def write_json(filename,d):
    obj = json.dumps(d,ensure_ascii=False,indent=4)
    f = open(filename,'w',encoding='utf-8-sig')
    f.write(obj)
    f.close()    

    
get_dicts()
