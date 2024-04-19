# f = open('poems.txt')
# t = f.read()
# if 'twinkle' in t:
#     print("Twinkle is present")
# else:
#     print("Twinkle is not present")
# f.close()

f = open('poems.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle present in poem")
else:
    print("Twinkle is not present")
f.close()