html = open("changetag.html")
data = html.readlines()
file = open("final.html", "a")
ansNumButton = 1
ansNumTag = 1
for line in data:
    if line.__contains__('BUTTON'):
        file.write(line.replace("BUTTON", "answer"+str(ansNumButton)))
        ansNumButton += 1
    elif line.__contains__('div id="answer"'):
        file.write(line.replace("answer", "answer"+str(ansNumTag)))
        ansNumTag += 1
    else:
        file.write(line)
