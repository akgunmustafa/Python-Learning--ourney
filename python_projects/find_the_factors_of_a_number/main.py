a = int(input("Enter a possitive integer: "))
b = 1
for i in range(a):

    if a % b == 0:
        print(str(b) + " is a factor of " + str(a))
    b = b + 1
