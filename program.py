import webbrowser, pyperclip, re

text = str(pyperclip.paste())
text = re.sub(r'\s+', '+', text)
print(text)
webbrowser.open('https://www.google.com/maps/dir//' + text)