import json

filename = "d:\VadZim\Python\ORMEDIA_Python\city.list.json\city.json"

with open(filename, encoding='utf-8') as json_file:
    json_sity = json.load(json_file)
    n = 0
    for i in json_sity:
        if i["country"] == "BY":
            print(i["name"])
            n += 1
    print(n)