print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


all_name = name1 + name2
lname = all_name.lower()

t = lname.count("t")
r = lname.count("r")
u = lname.count("u")
e = lname.count("e")

true = t + r + u + e

l = lname.count("l")
o = lname.count("o")
v = lname.count("v")
e = lname.count("e")

love = l + o + v + e
Love1 = str(love)
True1 = str(true)

Score = int(True1 + Love1)

# print (Score)

if (Score < 10) or (Score > 90):
    print(f"Your score is {Score}, you go together like coke and mentos.")
elif (Score >= 40) and (Score <= 50):
    print(f"Your score is {Score}, you are alright together.")
elif (Score < 15):
    print("RUN !")
else:
    print(f"Your score is {Score}.")