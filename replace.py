import os
import glob

directory = r"c:\Users\Administrator\Downloads\stitch_european_megalopolis_explorer\stitch_european_megalopolis_explorer"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file in html_files:
    # Skip index.html since we are going to overwrite it with the Three.js landing page anyway
    if file.endswith("index.html"):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the Conectare button
    # The button looks like: <button class="...neo-raised...">Conectare</button>
    # We will use regex to remove any button containing the exact text "Conectare"
    import re
    # Remove the entire button element containing "Conectare"
    content = re.sub(r'<button[^>]*>Conectare</button>', '', content)
    
    # Replace links to index.html with acasa.html (except in the landing page, which we skipped)
    content = content.replace('href="index.html"', 'href="acasa.html"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Replacement complete.")
