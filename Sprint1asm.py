quit = True
principles = []
principle_des = []
while quit:
    print("Welcome to the physics search board! Please input your choice: \n 1: add a principle \n 2: Search a principle \n 3: Print last inputted principle \n 4: print all principles \n 5: quit")
    choice = input("please input your choice: ")
    if choice == "1":
        new_principle = input("Please write the name of your new principle: ")
        new_des = input("Please write the description: ")
        indx = 0
        found = 0
        while indx < len(principles):
            if principles[indx] == new_principle:
                found = 1
            indx += 1
        if found != 0:
            print("I am sorry your principle has already been entered")
        else:
            principles.append(new_principle)
            principle_des.append(new_des)
    if choice == "2":
        search = input("Please input the principle you wish to search for: ")
        indx = 0
        found = -1
        while indx < len(principles):
            if principles[indx] == search:
                found = indx
                print("Principle Found")
            indx += 1
        if found != -1:
            print(principle_des[found])
        else:
            print("I am sorry that principle has not been entered")
    if choice == "3":
        if len(principles) == 0:
            print("Please input a principle first")
        else: 
            print("here is the last inputted principle \n" + principles[len(principles)-1] + "\n" + principle_des[len(principle_des)-1])
    if choice == "4":
        indx = 0
        while indx < len(principles):
            print(" " + principles[indx] + ": " + principle_des[indx] + "\n")
            indx+=1
    if choice == "5":
        quit = False