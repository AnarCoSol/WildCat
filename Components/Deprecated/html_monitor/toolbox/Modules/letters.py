from Text_manipulator import Text_manipulator

tm = Text_manipulator()

raw = tm.Read("/root/letters.txt")
y = raw.split("\n")
ax = 0
bx = 7
letters = list()
while True:
    letter = str()
    for ay in y:
        letter += ("\n" + ay[ax:bx])
    print letter
    letters.append(letter)
    ax += 7
    bx += 7
