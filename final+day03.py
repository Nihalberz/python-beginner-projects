# num=int(input("which number u wanna choose?"))

# if num % 2 == 0:
#     print("correct even number")
# else:
#     print("not a even number")


# print("Welcome to the rollercoaster")
# bill=0

# height=int(input("Tell me Your height in cm .?"))
# if height>=200:
#     print(" u can ride")


#     Age=int(input("tell me how old are u.?"))

#     if Age>=19:
#         bill=12
#         print("u have to pay $12. ")

#     elif Age >=10 and Age <=15:
#        bill=5
#        print("u have to pay $5")
#     else:
#        bill=7
#        print("U have to pay $7. ")

#     photos = (input("you want to click the photos.? yes or No"))

#     if photos==("yes"):
#         total_bill=int(bill)+5
#         print("U have to pay $5 for one.")
#     else:
#         total_bill=bill
#         print("don't worry u have to without Pic")
# else:
    
#     print("increase the height before riding")

# print(f"Your total bill would be {total_bill}")

# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# if bmi >18.5:
#     print("under weight")
# elif bmi>18.5 and bmi<25:
    
#     print("normal weight")
# else:
#     print("over weight")




# print("welcome to pizza deliveries. ")
# size=input("which size of pizza do u want. S , M , L ?")
# bill=0
# if size=="s":
#     bill=15
#     print("you have to pay $15")
# elif size=="m":
#     bill=20
#     print("you have to pay $20")
# elif size=="l":
#     bill=20
#     print("you have to pay $25")
# else:
#     print("you type the wrong input")
# pepperoni=input("Do you want to add some pepperoni on your pizza.? Y or N")
# if pepperoni=="y":
#     bill+=5
#     print("you have to pay +2$ extra for pepperoni")

# elif pepperoni=="n":
#     print("Okay Not an Issue")

# extra_cheese=input("Do you want to add some extracheese on your pizza.? Y or N")
# if extra_cheese=="y":
#     bill+=1
#     print("you have to pay +2$ extra for pepperoni")

# elif extra_cheese=="n":
#     print("Okay Not an Issue , Move on Bill Counter")
# print(f"your ${bill}")



#     LAST PROJECT OF DAY 03






print("Welcome to Treasure Island \
Your mission is to find the treasure.")
direction=input("which direction you would choose.? LEFT OR RIGHT")
if direction=="left":
    print("Thanks to choose left side\
    move on next part ")
    swim_or_wait=input("choose one  SWIM OR WAIT")
    if swim_or_wait=="wait":
        print("Thanks for choosing wait")

        door=input("which one side of door u would u prefer Yellow , Blue , Red or Right")
        if door =="red":
         print("Burned by fire\
                Game Over.")
        elif door =="yellow":
              print("You Win!")
        elif door=="blue":
              print("Eaten by beasts\
                Game Over.")
    elif swim_or_wait=="swim":
        print("GAme OVer")   
elif direction=="right":
    print("Fall into a hole.\
Game Over.")
