def game():
    return 26

score = game()
with open("hiscore.txt") as f:
    hiScore = f.read()
    
if hiScore=='':
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiScore)<score :
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

# def game():
#     return 44677

# score = game()
# with open("hiscore.txt") as f:
#     hiscorestr = f.read()
    
# if hiscorestr=='':
#     with open("hiscore.txt", "w") as f:
#         f.write(str(score))

# elif int(hiscorestr)<score :
#     with open("hiscore.txt", "w") as f:
#         f.write(str(score))
    
    
