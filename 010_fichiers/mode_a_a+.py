with open("test.txt", "a+") as f:
    f.seek(0)
    print(f.read())
# mode a : ouverture en ecriture seule
# mode a+ : ouverture en lecture/ecriture
# si le fichier n'existe pas => il le crée
# on ne vide pas le fichier avant les opérations
# on place le curseur au fin du fichier
