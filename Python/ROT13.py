"""How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc. Test examples:

rot13("EBG13 rknzcyr.") == "ROT13 example.";
rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!" """

def rot13(message):
    solution=""
    for i in range(len(message)):
        if type(message[i])==str and (ord(message[i])>=110 and ord(message[i])<=122) or (ord(message[i])>=78 and ord(message[i])<=90) :
            solution+=chr(ord(message[i])-13)  
        elif type(message[i])==str and( ord(message[i])>=97 and ord(message[i])<110) or  (ord(message[i])>=65 and ord(message[i])<=77):
            solution+=chr(ord(message[i])+13)    
        else:
            solution+=message[i]
    return solution
                
