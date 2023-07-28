import markdown
with open('README.md', 'r', encoding='utf-8', errors='ignore') as f:
    tempMd = f.read()

tempHtml = markdown.markdown(tempMd)
with open('readme.html', 'w') as f:
    f.write(tempHtml)