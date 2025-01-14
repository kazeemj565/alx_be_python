i = 0
j = 0
size = int(input("Enter the size of the pattern: "))
while i < size:
    print("*" * size)
    for j in range(i + 1):
        print("*", end="")
    i += 1
