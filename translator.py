import os

source = "A:\\Download\\CK2Translator\\BoPItalia Trad. Ita Ck2 2.8.3.4\\localisation\\"
translated = "A:\\Download\\CK2Translator\\BoPItalia Trad. Ita Ck2 3.0.1.1\\localisation\\"

destination_path = "A:\\Download\\CK2Translator output\\"

# gestione cartelle
if not os.path.exists(destination_path):
    os.makedirs(destination_path)

destination_name = "result.csv"
destination = destination_path + destination_name

final_result = open(destination, "w")
final_result.write(
    "Nome del file; Elenco di key modificate o aggiunte in 3.0.1.1; Numero file in 28.8.3.4;Numero file in "
    "3.0.1.1;Note\n")

final_result.write(";;" + str(len(os.listdir(source))) + ";" + str(
    len(os.listdir(
        translated))) + ";le directory vengono considerate come file, ove scritto -1 significa che è presente una "
                        "directory, quindi il conto finale va modficato\n")

# per ogni file all'interno della cartella localisation sorgente
for filename in os.listdir(source):
    # se il file è una directory lo ignoro
    if os.path.isdir(source + filename):
        print(source + filename + " è una directory")
        file_is_a_dir_res = filename + ";;-1"
        if os.path.exists(translated + filename) and os.path.isdir(translated + filename):
            file_is_a_dir_res += ";-1;è una directory presente in entrambe le versioni\n"
        else:
            file_is_a_dir_res += ";;è una directory non presente in 3.0.1.1\n"
        final_result.write(file_is_a_dir_res)
        continue

    print("Analisi file: " + filename)
    if os.path.exists(translated + filename):
        final_result.write(filename + ";\n")
        try:
            # apro il file di nome filename nella cartella sorgente
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

            # controllo che ogni elemento della prima colonna sia all'interno della lista, se non ci sta scrivo su file
            print("Linee non presenti in " + filename + " versione 3.0.1.1:")
            print("                                                 ")
            for line in tradotto.readlines():
                line = line.split(';')
                if line[0] not in keywords:
                    print(line[0])
                    final_result.write(";" + line[0] + "\n")
            print("                                                 ")
        except UnicodeDecodeError:
            print("Errore encode file" + filename + " ignorato")
            final_result.write(";Errore encode file ignorato\n")
    else:
        final_result.write(";File non trovato in nuova versione\n")

final_result.close()
