import re
turkicAlphabet ={
    "A" : "𐰀",
    "AB" : "𐰉",
    "EB" : "𐰋",
    "V" : "𐰋",
    "AÇ" : "𐰲",
    "C" : "𐰲",
    "J" : "𐰲",
    "EÇ" : "𐰱",
    "AD" : "𐰑",
    "ED" : "𐰓",
    "E" : "𐰀",
    "AG" : "𐰍",
    "EG" : "𐰏",
    "Ğ" : "𐰏",
    "I" : "𐰃",
    "İ" : "𐰃",
    "AK" : "𐰴",
    "EK" : "𐰚",
    "H" : "𐰚",
    "AL" : "𐰞",
    "EL" : "𐰠",
    "M" : "𐰢",
    "AN" : "𐰣",
    "EN" : "𐰤",
    "O" : "𐰆",
    "U" : "𐰆",
    "Ö" : "𐰇",
    "Ü" : "𐰇",
    "P" : "𐰯",
    "F" : "𐰯",
    "AR" : "𐰺",
    "ER" : "𐰼",
    "AS" : "𐰽",
    "ES" : "𐰾",
    "Ş" : "𐱁",
    "AT" : "𐱃",
    "ET" : "𐱅",
    "T" : "𐱅",
    "AY" : "𐰖",
    "EY" : "𐰘",
    "Z" : "𐰔",
    "ANÇ" : "𐰨",
    "ANG" : "𐰭",
    "ANT" : "𐰦",
    "ANY" : "𐰪",
    "ALT" : "𐰡",
    "IK" : "𐰶",
    "UK" : "𐰸",
    "ÜK" : "𐰜",
    " " : ":"
}

def getText():
    try:
        text=input("Metni giriniz")
        if re.search("[X,x,W,w,Q,q]",text):
            raise Exception("Metin X,W,Q harflerini içeremez")
        upperText=text.upper()
    except Exception as e:
        print(f"Hata: {e}. Lütfen tekrar deneyin.")
        getText()
    return upperText
    

def translateText():
    splitted = list(getText())
    reversed_list = splitted[::-1]
    reversed_text = ''.join(reversed_list)
    translated_text=""
    for char in reversed_text:
        if char in turkicAlphabet:
            translated_text += turkicAlphabet[char]
        else:
            translated_text += char 

    return translated_text

a =translateText()
with open ("text.txt","a", encoding="utf-8",) as file:
    file.write(a + "\n")


