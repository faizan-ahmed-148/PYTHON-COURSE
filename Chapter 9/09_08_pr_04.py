# with open("sample.txt") as f:
#     content = f.read()

# content = content.replace("donkey", "$%^@$^#")

# with open("sample.txt", "w") as f:
#     f.write(content)

with open("sample.txt") as f:
content = f.read()

content = content.replace("he", "$%^@$^#")

with open("sample.txt", "w") as f:
f.write(content)