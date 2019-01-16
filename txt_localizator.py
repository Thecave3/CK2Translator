# dati i file dictionary.csv e 00_customizable_localisation_IT.txt, genero un file di nome
# 00_customizable_localisation_IT_result.txt avente le righe della colonna 0 di dictionary.csv invece che le righe
# della colonna 3 di dictionary.csv.  per far si che ciò accada correttamente la riga 0 colonna 0 deve corrispondere
# alla traduzione di riga 0 colonna 3
working_directory = "A:\\Download\\CK2Translator\\Lingua\\"
working_subdirectory = "customizable_localisation\\"
dictionary_filename = "dictionary.csv"
source_filename = "00_customizable_localisation_IT.txt"

source = working_directory + working_subdirectory + source_filename

destination_path = "A:\\Download\\CK2Translator output\\"
destination_name = "00_customizable_localisation_IT_result.txt"
destination = destination_path + destination_name

translation_table = {}

dictionary = open(working_directory + dictionary_filename, 'r', encoding='ansi')

for line in dictionary:
    linea = line.strip('\n').split(';')
    if len(linea) > 4:
        translation_table[linea[3]] = linea[0]

source = open(source, 'r', encoding='ansi')
output_file = open(destination, 'w', encoding='ansi')

for line in source.readlines():
    new_line = ""
    for key in translation_table.keys():
        if key in line:
            new_line = line.replace(key, translation_table[key])
    output_file.write(new_line)

dictionary.close()
source.close()
output_file.close()
