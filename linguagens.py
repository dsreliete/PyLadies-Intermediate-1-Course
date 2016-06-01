linguagens = ['Java', 'JavaSript', 'PHP', 'C', 'Python']
tam = len(linguagens)
i = 1
while i < tam:
    language = linguagens[i]
    if language.startswith('P'):
        print(language.upper())
    i += 1



for i in linguagens:
    if i.startswith('P'):
        print(i.upper())

