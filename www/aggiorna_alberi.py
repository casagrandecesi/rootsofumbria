import json

# Leggiamo il file JSON originale
with open("alberi_rilevante_interesse.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Set di vocali (usato per il controllo sulla prima lettera della località)
vowels = set("AEIOU")

# Processiamo ogni feature aggiungendo il campo "nome"
for feature in data.get("features", []):
    props = feature.get("properties", {})
    specie = props.get("specie", "").strip()
    localita = props.get("localita", "").strip()
    if not specie or not localita:
        continue
    # Se "specie" contiene " DEL " allora prendiamo la parte precedente
    if " DEL " in specie:
        specie_part = specie.split(" DEL ")[0].strip()
    else:
        specie_part = specie
    # Controlliamo se la località inizia con una vocale
    if localita[0].upper() in vowels:
        connector = " DELL'"
    else:
        connector = " DI "
    # Costruiamo il nuovo campo "nome"
    props["nome"] = specie_part + connector + localita

num_features = len(data.get("features", []))
print(f"{num_features} alberi elaborati")

# Salviamo il file JSON modificato
with open("alberi_rilevante_interesse_modified.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
