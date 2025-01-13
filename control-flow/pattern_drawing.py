size = int(input("Enter the size of the pattern: "))
while size < 6:
    for i in range(size):
        print("*", end="")
    print('*')
    size += 1