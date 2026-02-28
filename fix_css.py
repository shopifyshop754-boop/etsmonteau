with open("/Users/macbookair/Ets Monteaux/style.css", "r") as f:
    content = f.read()
    
# Update background-image path as well in style.css
content = content.replace("url('./assets/Acceuil-1.jpg')", "url('./Acceuil-1.jpg')")

with open("/Users/macbookair/Ets Monteaux/style.css", "w") as f:
    f.write(content)
