import re
def gettext():
    f = open('text.txt', 'r', encoding = 'utf-8')
    text = f.read()
    f.close()
    return text

def getinitnames(text):
    result = re.findall(r'([А-ЯЁ]\.\s[А-ЯЁ][^\s|\W|\d]+)', text)
    result1 = re.findall(r'[А-ЯЁ]. [А-ЯЁ]. [А-ЯЁ][а-яё]+', text)
    for el in result:
        print(el)
    for el2 in result1:
        print(el2)


def getfull(text):
    result = re.findall(r'([А-ЯЁ][а-яё]\\s[А-ЯЁ][а-яё]+)', text)
    for el in result:
        print(el)
        
def main():
    num = gettext()
    getinitnames(num)
    getfull(num)
   

main()

