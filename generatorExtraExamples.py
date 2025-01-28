import string

# gera lower case English letters

def letters():
  for caracteres in string.ascii_lowercase:
    yield caracteres


for letras in letters():
  print(letras)