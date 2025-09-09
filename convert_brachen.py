import json

# Schritt 1: Alte Datei laden
with open('BrachenData.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Schritt 2: Neue, flache Struktur erzeugen
def flatten_entry(entry):
    return {
        'Nr': entry.get('Lfd. Nr.', ''),
        'WZ_Code': entry.get('WZ 2008\nKode', ''),
        'Bezeichnung': entry.get('WZ 2008 - Bezeichnung\n(a', {}).get('n', {}).get('g', {}).get(' = anderweitig nicht genannt)', ''),
        'ISIC_Rev4': entry.get('ISIC\nRev', {}).get(' 4', '')
    }

flat_data = [flatten_entry(e) for e in data]

# Schritt 3: Neue Datei speichern
with open('BrachenData_flat.json', 'w', encoding='utf-8') as f:
    json.dump(flat_data, f, ensure_ascii=False, indent=2)

print('Umwandlung abgeschlossen! Die neue Datei heißt BrachenData_flat.json.')
