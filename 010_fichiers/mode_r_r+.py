with open("test.txt", "r+") as f:
    f.read()
# mode r : ouverture en lecture seule
# mode r+ : ouverture en lecture/ecriture
# si le fichier n'existe pas => exception (FileNotFoundError)
# le curseur se place au début du fichier
