from typing import SupportsIndex
import unicodedata
"""vstup = unicodedata.normalize('NFKD',inp[2:-2].lower())
only_ascii = str(vstup.encode('ASCII', 'ignore'))
print(vstup)
print(only_ascii)"""

def mtl_translator(lat_to_morse,vstup):
    pismeno = str()
    vystup = str()
    for _ in range(len(vstup)):
        if vstup[_] != '/' and vstup[_] != " ":
            pismeno += vstup[_]
        else:
            for key in lat_to_morse:
                if pismeno == key:
                    vystup += str(lat_to_morse[pismeno])
            pismeno = str()
            if vstup[_-1] == '/':
                if vstup[_-2] == '/':
                    vystup = vystup[:-1]
                    vystup += '. '
                else:
                    vystup += ' '
    if (len(pismeno))>0:
        vystup += str(lat_to_morse[pismeno])
    c = vystup[0].capitalize()
    vystup = vystup.replace(vystup[0],c,1)
    for _ in range(len(vystup)):
        if vystup[_] == '.':
            try:
                c = vystup[_+2].capitalize()
                vystup = vystup.replace(vystup[_+2],c,1)
            except IndexError:
                pass
    return vystup
def ltm_translator(morse_to_lat,vstup):
    pismeno = str()
    vystup = str()
    for _ in range(len(vstup)):
        if vstup[_] == " ":
            if vstup[_-1] == ".":
                pass
            else:
                vystup += str('/')
        elif vstup[_] == ".": 
            vystup += str('//')      
        else:    
            for key in morse_to_lat:
                if vstup[_] == key:
                    vystup += str(morse_to_lat[vstup[_]])
                    vystup += str('/')
    return vystup

#Načtení vstupního souboru
try:
    with open ('vstup.txt', encoding="utf-8") as file1:   #,\
        #open ('vystup.txt', encoding="utf-8") as file2:
        inp = str(file1.readlines())    #POZOR JAKO ZNAKY SE UKLÁDÁ I ZAČÁTEK - [' - A KONEC - '] - TAKŽE BACHA NA TO A OŘÍZNOUT TO
except IOError:
    print("Chyba při načtení vstupu. Ve složce s programem musí být obsažen soubor 'vstup.txt'.")
    exit()

vstup_a = str(inp[2:-2].lower())
vstup = unicodedata.normalize('NFKD',vstup_a)
print(vstup_a)
print(vstup)
vystup = str()
l = []
lat_to_morse = {}
morse_to_lat = {
'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--',
'n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..',
'1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-...','7':'--...','8':'---..','9':'----.','0':'-----'}
for key, val in morse_to_lat.items():
    lat_to_morse[val] = key

if vstup[0] == '.' or vstup[0] == '-':
    vystup = mtl_translator(lat_to_morse,vstup)
else:
    vystup = ltm_translator(morse_to_lat,vstup)
print("výstup",vystup)
print(len(vstup))
       
    #if vstup[_] == "." or vstup[_] == "," or vstup[_] == "/":
     #   print("test",_)
        





    #else