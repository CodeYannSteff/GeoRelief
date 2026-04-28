import os
import glob
import re

directory = r"c:\Users\Administrator\Downloads\stitch_european_megalopolis_explorer\stitch_european_megalopolis_explorer"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file in html_files:
    if file.endswith("landing.html"):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the Conectare button from anywhere if it still exists
    content = re.sub(r'<button[^>]*>Conectare</button>', '', content)
    
    # Change links pointing to acasa.html back to index.html
    content = content.replace('href="acasa.html"', 'href="index.html"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Restored links to index.html and ensured Conectare is removed.")
