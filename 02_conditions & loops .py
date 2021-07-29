age = 18
if age >120 or age< 1:
    print("you are bot")
elif age > 18:
    print("you are adult")
else:
    print("you are young")

#page 46 in the python book

# compare bollian valuable:
x = True
if x == True:
    print("is true!")
x = False
if x is True:
    print("true")

elif x is False:
    print("now its working")
x = True
if x:
    print ("without compare")
x = False
if not x:
    print (x)
# The different between is and == ,
# is that the uses in 'is' make a *deep* compare - between the two adresses of the variables
#  uses in "==" make a low compare, between the values only.

# fibonachi series:
a=0
b=1
while (b+a) < 10000:
    print(b+a," , ")
    x = a
    a = b
    b = b+x

# for 

for i in range(0):
    name = input("your name is:")
    print (name, " ")

for i in range(1,100,1):
    if (i%7 == 0):
        print(i, " ")