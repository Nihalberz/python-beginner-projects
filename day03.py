# num=int(input("which number u wanna choose?"))

# if num % 2 == 0:
#     print("correct even number")
# else:
#     print("not a even number")


print("Welcome to the rollercoaster")
bill=0

height=int(input("Tell me Your height in cm .?"))
if height>=200:
    print(" u can ride")


    Age=int(input("tell me how old are u.?"))

    if Age>=19:
        bill=12
        print("u have to pay $12. ")

    elif Age >=10 and Age <=15:
       bill=5
       print("u have to pay $5")
    else:
       bill=7
       print("U have to pay $7. ")

    photos = (input("you want to click the photos.? yes or No"))

    if photos==("yes"):
        total_bill=int(bill)+5
        print("U have to pay $5 for one.")
    else:
        total_bill=bill
        print("don't worry u have to without Pic")
else:
    
    print("increase the height before riding")

print(f"Your total bill would be {total_bill}")

# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# if bmi >18.5:
#     print("under weight")
# elif bmi>18.5 and bmi<25:
    
#     print("normal weight")
# else:
#     print("over weight")