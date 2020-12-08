a = int(input("Starting Number : "))
b = int(input("Ending Number : "))
print("Prime numbers between", a, "and", b, "are:")
for i in range(a, b + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
