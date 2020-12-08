import random
stert_value=int(input("please enter the start value : "))
end_value=int(input("please enter the end value : "))
print(" ")
ans=random.randint(stert_value,end_value)
b = int(input("guess a number : "))
print(" ")
if b == ans:
    print("wow you guessed it first time !")
elif (b!= ans)and(b!=0)and(stert_value<=b<=end_value):
    b = 0
    while b != ans:
        b = int(input("guess again !: "))
        print(" ")
        if b != ans:
            if b == 0:
                print("meet you again ! bye!!!")
                break
            elif b > ans:
                print("please guess a lower number !")
            elif b < ans:
                print("please guess a higher number !")
        else:
            print("finally you got it correct !")
elif b==0:
    print("meet you again ! bye!!!")
else:
    print("please guess within the range !")