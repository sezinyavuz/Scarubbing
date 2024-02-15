error = True
while error:
    print("""
<-----RULES----->
1. BRUSH DOWN
2. BRUSH UP
3. VEHICLE ROTATES RIGHT
4. TURN LEFT
5. MOVE UP TO X
6. JUMP
7. REVERSE DIRECTION
8. VIEW THE MATRIX
0. EXIT
""")

    x = input("Please enter the commands with a plus sign (+) between them.")

    y = x.split("+") #input command list

    for i in y[1:]:

        if not i.startswith("5_"):
            if int(i) < 0 or int(i) > 8 :
                error = True
                break
            else:
                error = False

matrix = []
y[0] = int(y[0])
for i in range(0,y[0]):
    row = []
    for j in range(0,y[0]):
        row.append(" ")
    matrix.append(row)

list=[]

for i in range(0,y[0]+2):
    i= "+"
    list.append(i)

a = 0
b = 0
direction=1  # 1=sağ , 2 = aşağı , 3 = sola , 4 = yukarı
brush = False

for command in y:
    if command == "3" :
        direction +=1
        if direction > 4:
            direction -= 4

    if command == "4":
        direction -= 1
        if direction < 1:
            direction += 4

    if command == "7":
        direction += 2
        if direction > 4:
            direction -= 4

    if command == "1":
        brush = True
        matrix[b][a] = "*"
    if command == "2":
        brush = False

    if str(command).startswith("5") and brush == True:
        for i in range(int(command[2:])):
            if direction == 1 :
                a += 1
                if a > y[0]-1:
                    a = a % y[0]
                matrix[b][a] = "*"

            if direction == 2:
                b += 1
                if b > y[0]-1:
                    b = b % y[0]
                matrix[b][a] = "*"

            if direction == 3:
                a -= 1
                if a < 0:
                    a = y[0] - 1
                matrix[b][a] = "*"

            if direction == 4:
                b -= 1
                if b < 0:
                    b = y[0] - 1
                matrix[b][a] = "*"

    if str(command).startswith("5_") and brush == False:
        for i in range(int(command[2:])):
            if direction == 1 :
                a += 1
                if a > y[0]-1:
                    a = a % y[0]

            if direction == 2:
                b += 1
                if b > y[0]-1:
                    b = b % y[0]

            if direction == 3:
                a -= 1
                if a < 0:
                    a = y[0]-1

            if direction == 4:
                b -= 1
                if b < 0:
                    b = y[0]-1

    if command == "6":
        brush = False
        if direction == 1:
            a += 3
            if a >= y[0]:
                a = a % y[0]

        if direction == 2:
            b += 3
            if b >= y[0]:
                b = b % y[0]

        if direction == 3:
            a -= 3
            if a < 0:
                a = a + y[0]

        if direction == 4:
            b -= 3
            if b < 0:
                b = b + y[0]

    if command == "8":
        print(*list)
        for i in matrix:
            print("+", *i, "+")
        print(*list)
















