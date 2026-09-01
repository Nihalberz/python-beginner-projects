# num=int(input("which number u wanna choose?"))

# if num % 2 == 0:
#     print("correct even number")
# else:
#     print("not a even number")


# print("Welcome to the rollercoaster")
# height=int(input("Tell me Your height in cm .?"))
# if height>=200:
#     print(" u can ride")


#     Age=int(input("tell me how old are u.?"))

#     if Age>=19:
#            print("u have to pay $12. ")
#     elif Age >=10 and Age <=15:
#        print("u have to pay $5")
#     else:
#        print("U have to pay $7. ")
# else:
#     print("increase the height before riding")

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi >18.5:
    print("under weight")
elif bmi>18.5 and bmi<25:
    
    print("normal weight")
else:
    print("over weight")