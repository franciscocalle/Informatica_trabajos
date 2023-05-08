#!/usr/bin/env python3
import re 
def mail_correcto(string):
    return bool(re.search('^\w+[-_.]?\w*@[a-z]+\.[a-z]+$' ,string))
print(mail_correcto('salva_.9burgos@gmail.com'))

                
