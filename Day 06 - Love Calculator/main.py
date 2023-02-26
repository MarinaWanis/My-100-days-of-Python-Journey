# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

combined_names = name1 + name2

t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

true = t + r + u + e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

love = l + o + v + e

true_str = str(true)
love_str = str(love)
total = true_str + love_str

total = int(total)

if total <= 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together")
else:
    print(f"Your score is {total}")
