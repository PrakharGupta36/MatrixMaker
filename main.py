def matrix():
    width = int(input("Enter the width of the checkerbox : "))
    height = int(input("Enter the height of the checkerbox : "))
    
    if width < 0 or height < 0:
        print("Only +ve numbers")
        matrix()
    
    checkbox = []

    new_list = []
    new_list_2 = []

    w = 0 
    x = 1


    for i in range(width):
        x ^= 1
        new_list.append(x)

    for i in range(width):
        w ^= 1
        new_list_2.append(w)

    if height % 2 == 0:
        for j in range(int(height/2)):
            checkbox.append(new_list)
            checkbox.append(new_list_2)
        print()  # for a line break
        for z in checkbox:
            print(', '.join(map(str, z)))  # removing brackets from lists
    else:
        for j in range(height):
            checkbox.append(new_list)
            checkbox.append(new_list_2)
        print()  # for a line break
        for z in checkbox:
            print(', '.join(map(str, z)))  # removing brackets from lists
            checkbox.pop()


matrix()