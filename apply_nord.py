import os
import glob
import re

nord_config_and_style = """    <script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        background: "#2e3440",
                        surface: "#3b4252",
                        "surface-raised": "#434c5e",
                        primary: "#88c0d0",
                        secondary: "#81a1c1",
                        tertiary: "#5e81ac",
                        success: "#a3be8c",
                        error: "#bf616a",
                        warning: "#ebcb8b",
                        "on-background": "#eceff4",
                        "on-surface": "#e5e9f0",
                        "on-surface-variant": "#d8dee9",
                    },
                    fontFamily: {
                        sans: ["Plus Jakarta Sans", "sans-serif"],
                    }
                }
            }
        }
    </script>
    <style>
        body { background-color: #2e3440; color: #eceff4; font-family: 'Plus Jakarta Sans', sans-serif; }
        .neo-raised { background-color: #3b4252; box-shadow: 5px 5px 10px #272c36, -5px -5px 10px #4f586e; }
        .neo-pressed { background-color: #3b4252; box-shadow: inset 5px 5px 10px #272c36, inset -5px -5px 10px #4f586e; }
        .neo-interactive:hover { transform: translateY(-2px); box-shadow: 7px 7px 14px #272c36, -7px -7px 14px #4f586e; }
        .neo-interactive:active { transform: translateY(0); box-shadow: inset 4px 4px 8px #272c36, inset -4px -4px 8px #4f586e; }
        
        /* Typography overrides for Nord */
        h1, h2, h3, h4, h5, h6 { color: #eceff4 !important; }
        p, span, div { color: #d8dee9; }
        a { color: #88c0d0; transition: color 0.2s; }
        a:hover { color: #81a1c1; }
        
        /* Overrides for specific text utilities from before */
        .text-slate-800, .text-slate-700, .text-on-surface, .text-indigo-600, .text-indigo-700 { color: #eceff4 !important; }
        .text-slate-600, .text-slate-500, .text-on-surface-variant { color: #d8dee9 !important; }
        .text-primary { color: #88c0d0 !important; }
        .bg-[#e8eaf0], .bg-slate-900 { background-color: #3b4252 !important; }
        .bg-white { background-color: #3b4252 !important; }
    </style>"""

directory = r"c:\Users\Administrator\Downloads\stitch_european_megalopolis_explorer\stitch_european_megalopolis_explorer"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file in html_files:
    if file.endswith("landing.html"):
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the old config and style
    # We will use regex to find everything from <script id="tailwind-config"> to </style>
    pattern = re.compile(r'<script id="tailwind-config">.*?</style>', re.DOTALL)
    
    if pattern.search(content):
        content = pattern.sub(nord_config_and_style, content)
    else:
        # Fallback if the script id is missing or format is different
        print(f"Pattern not found in {file}, skipping...")
        
    # Replace inline colors that might clash with Nord
    content = content.replace("bg-[#e8eaf0]", "bg-surface")
    content = content.replace("text-indigo-600", "text-primary")
    content = content.replace("text-indigo-500", "text-secondary")
    content = content.replace("shadow-[6px_6px_12px_rgba(0,0,0,0.08),-6px_-6px_12px_rgba(255,255,255,0.6)]", "neo-raised")
    content = content.replace("shadow-[inset_4px_4px_8px_rgba(0,0,0,0.06),inset_-4px_-4px_8px_rgba(255,255,255,0.5)]", "neo-pressed")
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied Nord Theme to all HTML files.")
