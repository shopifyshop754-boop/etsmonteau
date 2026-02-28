import re

files = ["index.html", "services.html", "contact.html"]

for file in files:
    with open(f"/Users/macbookair/Ets Monteaux/{file}", "r") as f:
        content = f.read()

    # The user uploaded the images directly to the root of the repo, not in the assets folder!
    # Update paths from ./assets/image.jpg to just ./image.jpg
    content = content.replace('./assets/logo-transparent.png', './logo-transparent.png')
    content = content.replace('./assets/contact.jpg', './contact.jpg')
    content = content.replace('./assets/Acceuil-2.jpg', './Acceuil-2.jpg')
    content = content.replace('./assets/Acceuil-1.jpg', './Acceuil-1.jpg')
    
    with open(f"/Users/macbookair/Ets Monteaux/{file}", "w") as f:
        f.write(content)

