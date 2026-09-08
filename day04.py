import random
# random_number_0_to_1=random.randint(0,1)
# if random_number_0_to_1==0:
#     print("head")
# else:
#      print("tail")


 

# random_head_or_tail=random.randint(0,1)

# head_or_tail=input("choose one HEAD OR TAIL")
# if random_head_or_tail== 0:
#     print("head")

# elif random_head_or_tail==1:
#     print("tail")


#                Pay Bill Randomisation


# friends=["alice","Darlie","berz","berzillus","nirrali"]
# print(random.choice(friends))


# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)




# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1])
# print(dirty_dozen[1][1])






                # ROCK, PAPER ,SCISSOR
choices=["rock","paper","scissors"]
user_choice=input("Choose one ,ROCK , PAPER , SCISSORS:").lower()
computer_choice=random.choice(choices)
print("you choose:",user_choice)
print("Computer chose:", computer_choice)

if computer_choice==user_choice:
    print("DRAW")
elif computer_choice=="rock":
    if user_choice=="paper":
        print("You win")
    else:
        print("you lose")
elif computer_choice==("paper"):
    if user_choice==("scissors"):
        print("you win")
    else:
        print("you lose")
elif computer_choice=="scissors":
    if user_choice=="rock":
        print("you win")
    else:
        print("you lose")
else:
    print("invalid input")