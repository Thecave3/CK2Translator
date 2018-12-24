import os

source = "A:\\Programmi\\SteamLibrary\\steamapps\\common\\Crusader Kings II\\localisation\\"
translated = "A:\\Download\\BoPItalia Trad. Ita Ck2 2.8.3.4\\localisation\\"

test = "A:\\Download\\result.csv"

finalresult = open(test, "w")

finalresult.write("Nome del file; Elenco di key modificate\n")

# per ogni file all'interno della cartella localisation sorgente
for filename in os.listdir(source):
    # se il file è una directory lo ignoro
    if os.path.isdir(source + filename):
        continue

    print("Analisi file: " + filename)
    finalresult.write(filename + ";\n")
    try:
        # apro ilfile di nome filename nella cartella sorgente
        sorgente = open(source + filename, "r", encoding='ansi')
        # apro lo stesso file nella cartella tradotta
        tradotto = open(translated + filename, "r", encoding='ansi')

        # salvo tutta la prima colonna del file sorgente in una lista
        keywords = []
        for line in sorgente.readlines():
            line = line.split(';')
            keywords.append(line[0])

        # test di stampa
        # for key in keywords:
        #    print(key)

        # controllo che ogni elemento della prima colonna sia all'interno del dizionario, se non ci sta scrivo su file
        #
        print("Linee non presenti in " + filename + ":")
        #  print("                                                 ")
        for line in tradotto.readlines():
            line = line.split(';')
            if line[0] not in keywords:
                print(line[0])
                finalresult.write(";" + line[0] + "\n")
        # print("                                                 ")
    except UnicodeDecodeError:
        print("Errore encode file" + filename + " ignorato")
        finalresult.write(";Errore encode file ignorato\n")
    except FileNotFoundError:
        print("Errore file not found" + filename)
        finalresult.write(filename + ";Errore file non trovato\n")
finalresult.close()
