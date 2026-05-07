import os

files_to_update = [
    'index.html',
    'digsilent-powerfactory.html',
    'digsilent-applications.html',
    'digsilent-features.html',
    'target3001-main.html',
    'target3001-applications.html',
    'target3001-features.html'
]

old_block = """        <a href="#products">Products</a>
        <ul class="dropdown-menu">
          <li class="dropdown-group">
            <a href="#products">DIgSILENT PowerFactory</a>
            <ul>
              <li><a href="#products">Applications</a></li>
              <li><a href="#products">Features</a></li>
            </ul>
          </li>
          <li class="dropdown-group">
            <a href="#products">TARGET 3001!</a>
            <ul>
              <li><a href="#products">Applications</a></li>
              <li><a href="#products">Features</a></li>
            </ul>
          </li>"""

new_block = """        <a href="#products">Products</a>
        <ul class="dropdown-menu">
          <li class="dropdown-group">
            <a href="digsilent-powerfactory.html">DIgSILENT PowerFactory</a>
            <ul>
              <li><a href="digsilent-applications.html">Applications</a></li>
              <li><a href="digsilent-features.html">Features</a></li>
            </ul>
          </li>
          <li class="dropdown-group">
            <a href="target3001-main.html">TARGET 3001!</a>
            <ul>
              <li><a href="target3001-applications.html">Applications</a></li>
              <li><a href="target3001-features.html">Features</a></li>
            </ul>
          </li>"""

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated_content = content.replace(old_block, new_block)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"Updated {filename}")
    else:
        print(f"Skipped {filename} - not found")
