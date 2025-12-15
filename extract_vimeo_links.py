import json
import re
import csv

# Read the JSON file
with open('/Users/maximilianocalva/Documents/Antigravity/IDEBIO/Tutorias_G42.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Function to extract Vimeo ID from iframe content
def extract_vimeo_id(iframe_content):
    match = re.search(r'player\.vimeo\.com/video/(\d+)', iframe_content)
    return match.group(1) if match else None

# Function to recursively search for tabs with Vimeo links
def find_vimeo_sessions(obj, sessions=[]):
    if isinstance(obj, dict):
        # Check if this object has tabs
        if 'tabs' in obj and isinstance(obj['tabs'], list):
            for tab in obj['tabs']:
                if 'tab_title' in tab and 'tab_content' in tab:
                    vimeo_id = extract_vimeo_id(tab['tab_content'])
                    if vimeo_id:
                        sessions.append({
                            'title': tab['tab_title'],
                            'vimeo_id': vimeo_id,
                            'vimeo_url': f'https://vimeo.com/{vimeo_id}'
                        })
        
        # Recursively search in all values
        for value in obj.values():
            find_vimeo_sessions(value, sessions)
    
    elif isinstance(obj, list):
        for item in obj:
            find_vimeo_sessions(item, sessions)
    
    return sessions

# Extract all sessions
print("Extrayendo sesiones con enlaces de Vimeo...")
sessions = find_vimeo_sessions(data)

print(f"Se encontraron {len(sessions)} sesiones")

# Save to CSV
csv_file = '/Users/maximilianocalva/Documents/Antigravity/IDEBIO/Sesiones_Vimeo_G42.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'vimeo_id', 'vimeo_url'])
    writer.writeheader()
    writer.writerows(sessions)

print(f"Archivo CSV guardado en: {csv_file}")

# Also save to a text file for easy reading
txt_file = '/Users/maximilianocalva/Documents/Antigravity/IDEBIO/Sesiones_Vimeo_G42.txt'
with open(txt_file, 'w', encoding='utf-8') as f:
    f.write("SESIONES DEL DIPLOMADO EN BIODESPROGRAMACIÓN - GENERACIÓN 42\n")
    f.write("=" * 80 + "\n\n")
    for i, session in enumerate(sessions, 1):
        f.write(f"{i}. {session['title']}\n")
        f.write(f"   Vimeo URL: {session['vimeo_url']}\n")
        f.write(f"   Vimeo ID: {session['vimeo_id']}\n\n")

print(f"Archivo de texto guardado en: {txt_file}")
print("\n¡Extracción completada!")
