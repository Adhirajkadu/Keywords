r=int(input("Enter a range :"))

for i in range(r):
    if i % 20 == 0:
        print("twist")
    elif i % 15 == 0:
        print("test")
    elif i % 5 == 0:
        pass
    elif i % 3 == 0:
        print("buzz")
    else:
        print(i)