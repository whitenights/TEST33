import re
def gettext():
    f = open('text.txt', 'r', encoding = 'utf-8')
    text = f.read()
    f.close()
    return text

def getinitnames(text):
    result = re.findall(r'([А-Я]\.\s[А-Я][^\s|\W|\d]+)', text)
    for el in result:
        print(el)

def getfullnames(text):
    result = re.findall(r'([А-Я][^\s|\W|\d]\\s[А-Я][^\s|\W|\d]+)', text)
    for el1 in result:
        print(el1)

def main():
    num = gettext()
    getinitnames(num)
    getfullnames(num)
    
main()
