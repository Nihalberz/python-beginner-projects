import random
# student_scores=[120,129,123,1234,12345,55,5555,59905,59000,57839,3849,8476,]
# max=0
# for score in student_scores:
#     if score>max:
#         max=score
# print(max)




# total=0
# for number in range(1,101):
#     total+=number
# print(total)
    



# for number in range(1,101):
#     if number%3==0:
#         print("fizz")


       
#     elif number%5==0:
#          print("buzz")
#     elif number % 3==0 and number% 5==0:
#      print("fizzbuzz")
#     else :
#        print (number)


# def gukban(count):
#     while count!=100:
#       print(count)
#       count=count+1;
# gukban(0)




#                             Password generator
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number=['1','2','3','4','5','6','7','8','9']
symbol=['~' ',' , '!', '@', '$', '%', '^', '&,']
print("wellcome to password generator...")
nr_alpha=int(input("how many alphabet would u like to add in password.?"))
nr_number=int(input("how many number would u like to add in password.?"))
nr_symbol=int(input("how many symbol would u like to add in password.?"))
pasword=[]
for i in range(nr_alpha):
    pasword.append(random.choice(alphabet))
for i in range(nr_number):
    pasword.append(random.choice(number))
for i in range(nr_symbol):
    pasword.append(random.choice(symbol))
# random.shuffle(pasword)

# # print("your pasword is:",''.join(pasword))


# def gukban(count):
#     while count!=4500000:
#       print(count)
#       count=count+1
# gukban(0)




# x=['1','2','3','4','5','6','7','8','9']
# y=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# new=[]
# new.append(random.choice(x))
# new.append(random.choice(y))

# random.shuffle(new)

# print(new)