
import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print (re.search(patron, texto))
print(re.match(patron, texto))
print(re.findall(patron, texto))
print(re.search(patron, texto).group())
print(re.sub(patron, "###", texto))