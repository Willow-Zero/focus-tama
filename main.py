

displayVolume = [[" " for x in range(0,100)] for x in range(0,15)]


printDisplay(displayVolume):
    for x in displayVolume:
        for y in x:
            print(y,end="")
        print("\n")


