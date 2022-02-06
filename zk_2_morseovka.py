#Import of unicodedata module
import unicodedata

#Method for translate text from morse code to latin script
def mtl_translator(lat_to_morse,inp):
    char = str()
    outp = str()
    for i in range(len(inp)):
        if inp[i] != '/' and inp[i] != " ":
            char += inp[i]      #Adding comma or point to variable
        else:
            for key in lat_to_morse:
                if char == key:     #Asking if it the variable of commas and points are in a dictionary
                    outp += str(lat_to_morse[char])     #Adding value of dictionary on possition 'char'
                elif char not in lat_to_morse:
                    if char == str():   #Bug fix
                        pass
                    else:       #End of program if the variable isn't into dictionary
                        print("Char",char,"isn't in dictionary of morse code.")
                        exit()
            char = str()
            #Check if there is the end of word or sentence
            if inp[i-1] == '/':
                if inp[i-2] == '/':     
                    outp = outp[:-1]
                    outp += '. '    #End of sentence - adding point after word
                else:
                    outp += ' '     #End of word - adding space after word
    #Capital letter at the beginning of the first sentence
    if (len(char))>0:
        outp += str(lat_to_morse[char])
    c = outp[0].capitalize()
    outp = outp.replace(outp[0],c,1)
    #Capital letter at the beginning of the next sentence
    for j in range(len(outp)):
        if outp[j] == '.':
            try:
                c = outp[j+2].capitalize()
                outp = outp.replace(outp[j+2],c,1)
            except IndexError:
                pass
    return outp

#Method for translate text from latin script to morse code
def ltm_translator(morse_to_lat,inp):
    outp = str()
    for i in range(len(inp)):
        #Asking on the end of word or end of sentence
        if inp[i] == " ":
            if inp[i-1] == ".":
                pass
            else:
                outp += str('/')    #End of one letter
        elif inp[i] == ".": 
            outp += str('//')   #End of one word
        else:    
            #Asking it if letter is in dictionary 
            for key in morse_to_lat:
                if inp[i] == key:
                    outp += str(morse_to_lat[inp[i]])   #Adding combination of commos and points
                    outp += str('/')    #End of one letter
                elif inp[i] not in morse_to_lat:     #End of program if the letter isn't in dictionary
                    print("Char",inp[i],"isn't in the dictionary of morse code.")
                    exit()
    return outp

#Decode method
def decode(inp_0):
    inp_a = str(inp_0[2:-2].lower())
    inp_b = unicodedata.normalize('NFKD',inp_a)
    inp_c = str(inp_b.encode('ASCII', 'ignore'))
    inp = inp_c[2:-1]
    return inp

#Loading input data, her conversion and definiton the dictionary of morse code
try:
    with open ('input.txt', encoding="utf-8") as file1,\
        open ('output.txt',"w", encoding="utf-8") as file2:
        inp_0 = str(file1.readlines()) 
        inp = decode(inp_0)
        outp = str()
        lat_to_morse = {}
        morse_to_lat = {
        'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--',
        'n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..',
        '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-...','7':'--...','8':'---..','9':'----.','0':'-----'}

        #Creating reverse dictionary of morse code
        for key, val in morse_to_lat.items():
            lat_to_morse[val] = key

        #Choosing of translate type and calling method of choosen translate type
        if inp[0] == '.' or inp[0] == '-':
            outp = mtl_translator(lat_to_morse,inp)
        else:
            outp = ltm_translator(morse_to_lat,inp)
            
        #Printing results in the terminal
        if outp[0] == "." or outp[0] == "-":
            print("Text in latin script:",inp_0[2:-2])
            print("Text in morse code:",outp)
        else:
            print("Text in morse code:",inp_0[2:-2])
            print("Text in latin script:",outp)
            
            
            
        #Writing output to a file 'output.txt'
        file2.write(outp)

except IOError:
    print("Loading file Error. In folder with program must be a file 'input.txt'.")
    exit() 