size = int(input("Enter the size of the pattern: "))
while size < 5:
    print("*" * size)
    for i in range(size):
        print("*", end="")
        # print("*" * i)
    print()
    size += 1 