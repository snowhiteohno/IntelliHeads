import os

subpages = [
    'digsilent-powerfactory.html',
    'digsilent-applications.html',
    'digsilent-features.html',
    'target3001-main.html',
    'target3001-applications.html',
    'target3001-features.html'
]

# 1. Update index.html
if os.path.exists('index.html'):
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix logo link
    content = content.replace('<a class="nav-logo" href="#">', '<a class="nav-logo" href="index.html">')
    # Fix Home link in footer
    content = content.replace('<li><a href="#">Home</a></li>', '<li><a href="index.html">Home</a></li>')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Update sub-pages
for page in subpages:
    if os.path.exists(page):
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace('<a class="nav-logo" href="#">', '<a class="nav-logo" href="index.html">')
        content = content.replace('<li><a href="#">Home</a></li>', '<li><a href="index.html">Home</a></li>')
        content = content.replace('href="#hero"', 'href="index.html#hero"')
        content = content.replace('href="#about"', 'href="index.html#about"')
        content = content.replace('href="#services"', 'href="index.html#services"')
        content = content.replace('href="#events"', 'href="index.html#events"')
        content = content.replace('href="#contact"', 'href="index.html#contact"')
        
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)

print("Navigation links fixed.")
