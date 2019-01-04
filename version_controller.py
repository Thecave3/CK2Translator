import os

# confronta le due versioni della traduzione ed evidenzia le differenze in un file csv di output

older_version_path = "A:\\Download\\CK2Translator\\BoPItalia Trad. Ita Ck2 2.8.3.4\\localisation\\"
newer_version_path = "A:\\Download\\CK2Translator\\BoPItalia Trad. Ita Ck2 3.0.1.1\\localisation\\"

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

final_result.write(";;" + str(len(os.listdir(older_version_path))) + ";" + str(
    len(os.listdir(
        newer_version_path))) + ";le directory vengono considerate come file, ove scritto -1 significa che è presente "
                                "una "
                                "directory, quindi il conto finale va modificato\n")

# per ogni file all'interno della cartella localisation sorgente
for filename in os.listdir(older_version_path):
    # se il file è una directory lo ignoro
    if os.path.isdir(older_version_path + filename):
        print(older_version_path + filename + " è una directory")
        file_is_a_dir_res = filename + ";;-1"
        if os.path.exists(newer_version_path + filename) and os.path.isdir(newer_version_path + filename):
            file_is_a_dir_res += ";-1;è una directory presente in entrambe le versioni\n"
        else:
            file_is_a_dir_res += ";;è una directory non presente in 3.0.1.1\n"
        final_result.write(file_is_a_dir_res)
        continue

    print("Analisi file: " + filename)
    if os.path.exists(newer_version_path + filename):
        final_result.write(filename + ";\n")
        try:
            # apro il file di nome filename nella cartella sorgente
            vecchia_versione = open(older_version_path + filename, "r", encoding='ansi')
            # apro lo stesso file nella cartella tradotta
            nuova_versione = open(newer_version_path + filename, "r", encoding='ansi')

            # salvo tutta la prima colonna del file sorgente in un dizionario
            keywords = {}
            for line in vecchia_versione.readlines():
                line = line.split(';')
                keywords[line[0]] = 0  # assegno il valore 0 per controllare se non sia stata rimossa

            # test di stampa
            # for key in keywords:
            #    print(key)

            # controllo che ogni elemento della prima colonna sia all'interno della lista, se non ci sta scrivo su
            # file perchè significa che la stringa è stata modificata o aggiunta
            print("Linee non presenti in " + filename + " versione 3.0.1.1:")
            print("                                                 ")
            for line in nuova_versione.readlines():
                line = line.split(';')
                if line[0] not in keywords:
                    print(line[0])
                    final_result.write(";" + line[0] + "\n")
                keywords[line[0]] = 1  # è presente nella versiona nuova aggiorno il valore del dizionario
            print("                                                 ")
            # se la stringa non ha avuto un accesso significa che nella nuova versione è stata rimossa
            for key in keywords.keys():
                if keywords[key] == 0:
                    final_result.write(";" + key + ";;; stringa rimossa in nuova versione\n")

        except UnicodeDecodeError:
            print("Errore encode file" + filename + " ignorato")
            final_result.write(";Errore encode file ignorato\n")
    else:
        final_result.write(";File non trovato in nuova versione\n")

final_result.close()
