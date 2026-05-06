a = input("Enter a word:  ")

for i in a:
    if (i == "A"):
        print("A found")
        break
    elif(i == "a"):
        print("a found")
        break
    else:
         print("A not found")