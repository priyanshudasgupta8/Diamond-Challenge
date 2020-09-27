import os
import time

while True:
    prompt = int(input('Enter the number of rows: ').strip())
    num = int(prompt / 2)
    print()

    n = 1
    for i in range(1, num + 1):
        for j in range(1, num - i + 1):
            print(end=" ")

        for cols in range(i, 0, -1):
            print(n, end=" ")
            n += 1

            if n % 10 == 0 or n > 10:
                n = 0

        print()

    for i in range(num, 0, -1):
        for j in range(0, num - i):
            print(end=" ")

        for cols in range(i, 0, -1):
            print(n, end=" ")
            n = n + 1

            if n > 10:
                n = 0
            elif n % 10 == 0:
                n = 0

        print()

    time.sleep(2.5)
    os.system("clear")  # Linux - OSX
    # os.system("clr") WINDOWS only
