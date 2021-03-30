firstQuest = ("This is the first path.")
secondQuest = ("This is the second path.")
thirdQuest = ("This is the third path.")
fourthQuest = ("This is the fourth path.")
fifthQuest = ("This is the fifth path.")
sixthQuest = ("This is the sixth path.")

choice1 = input("Go left or right? ")

if choice1 == ("left"):
    print(secondQuest)
    finalPath = ("right")

elif choice1 == ("right"):
    print(thirdQuest)
    finalPath = ("left")

print(fourthQuest)

if finalPath == ("left"):
    print(fifthQuest)
else:
    print(sixthQuest)