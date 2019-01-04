# dati i tre file ITA.csv, SPA.csv e 00_customizable_localisation_IT.txt, genero un file di nome
# 00_customizable_localisation_IT_result.txt avente al posto delle righe della colonna 0 di SPA.csv le righe della
# colonna 0 di ITA.csv per far si che ciò accada correttamente le righe di ITA.csv e quelle di SPA.csv devono essere
# una la traduzione dell'altra (riga 0 colonna 0 di ITA.csv corrisponde alla traduzione di riga 0 colonna 0 di SPA.csv)

working_directory = "A:\\Download\\CK2Translator\\Lingua\\"
working_subdirectory = "customizable_localisation\\"
spa_filename = "SPA.csv"
ita_filename = "ITA.csv"
source_filename = ""

destination_path = "A:\\Download\\CK2Translator output\\"
destination_name = "00_customizable_localisation_IT_result.txt"
destination = destination_path + destination_name
