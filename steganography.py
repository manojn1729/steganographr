from typing import List,Iterable

def strToBin(text: str) -> List[str]:
    binTest=[]
    return [bin(ord(i)).replace('0b','') for i in text]

def binToHide(data: List[str])-> str:
    return '\u2060'.join([i.replace('1','\u200D').replace('0','\u200C') for i in data])

def wrap(text: str, hideText: str) -> str:
    return text+'\u2060'+hideText

def unwrap(text: str) -> str:
    if text.find('\u2060')<0:
        return ""
    return text[text.find('\u2060')+1:]

def hideToBin(text: str) -> List[str]:
    return text.replace('\u200D','1').replace('\u200C','0').split('\u2060')

def binToStr(data: List[str]) -> str:
    if data==['']:
        return ''
    text=''
    for i in data: text+=chr(int(i,2))
    return text