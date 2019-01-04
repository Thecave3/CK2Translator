import requests
import json

# traduttore automatico che legge le stringhe da tradurre da un file csv
# ed invia una richiesta HTTP a yandex e salva il risultato un nuovo file

# apro il file ITA e
# per ogni riga
# se non inizia con string vai avanti
# se è già presente la traduzione o se la parte src contiene [ ] vado avanti
# altrimenti traduco la frase e riscrivo il file


working_directory = "A:\\Download\\CK2Translator\\Lingua\\"
endpoint_url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
headers = {'Cache-Control': "no-cache"}
# see the key on yandex
api_key = ""

valid_key_str = "String_IT"
black_list_str = "["

# print(response.text)
with open(working_directory + "ITA.csv", 'r') as src_file:
    dest_file = open(working_directory + "ITA_result.csv", 'w')
    dest_file.write(src_file.readline())
    for line in src_file:
        row = line.strip('\n').split(';')
        if valid_key_str in row[0]:
            if not row[1] and row[2]:
                if black_list_str in row[2]:
                    dest_file.write(line)
                else:
                    querystring = {"key": api_key,
                                   "text": row[2], "lang": "es-it", "format": "plain"}
                    response = requests.request("GET", endpoint_url, headers=headers, params=querystring)
                    print(response.text)
                    resp = json.loads(response.text)
                    result_str = ""
                    if resp["code"] == 200:
                        result_str += row[0] + ";" + resp["text"][0] + ";" + row[2] + "\n"
                    else:
                        result_str += row[0] + ";" + response.text + ";" + row[2] + "\n"
                    dest_file.write(result_str)

            else:
                dest_file.write(line)
        else:
            dest_file.write(line)

    dest_file.close()
    src_file.close()
