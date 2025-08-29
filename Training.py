
name = input('What isyour name? ')
fav_colour = input('What is your favourite colour? ')
print('Hi ' + name + ' loves ' + fav_colour)

Year_of_birth= input('Date of birth: ')
age = 2025 - int(Year_of_birth)
print(age)

#--------Weight Converter------------

Weight_lb = input("what is your weight in pounds? ")
Converter = float(Weight_lb) * 0.454
weight = str(Converter) 
print("your weight is " + weight + "Kg")


#-----------Strings/ Formatted strings-------------

First = 'David'
Last = 'Jubilee'
message = First + " [ " + Last + " ]" + " is a coder"
msg = f'{First} [{Last}] is a coder'
print(msg) 

#------------String Methods------------------------

course = "Python for Beginners"
print(len(course))
print (course.upper())
print (course.lower())
print(course.find('P'))
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course)
print(course.title())

#----------------Arithmetic Opetators--------------------
x = 10
x = x + 3
x *= 3
print(x)

#-----------------Round function-------------------------

x = 2.789
print(round(x))
print (abs(-2.12))


#----------------import math-----------------------------

print(math.factorial(5))
print(math.acosh(4))
print(math.exp(2))

#-------------------------If Statements------------------

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty water")

elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")

else:
    print("It's a lovely day!")

print("Enjoy your day!")
#------------------- More on If Statements-------------------
price = 1000000
good_credit = False
bad_credit = False

if good_credit:
    payment = 1000000 * 0.1
    print(payment)

elif bad_credit:
    payment1 = 1000000 * 0.2
    print(payment1)

else:
    print(" Your down payment is 1 Million Dollars")

price = 1000000
good_credit = True

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")

#---------------------------LOGICAL AND------------------------

has_high_income = True
has_good_credit = True

if has_high_income and good_credit:
    print("Eligible for a loan")

#--------------------------LOGICAL OR----------------------------

has_high_income1 = True
has_good_credit1 = False

if has_high_income1 or has_good_credit1:

    print("Eligible for a loan")

#----------------------------LOGICAL NOT---------------------------

has_good_credit = True
has_no_criminal_record = False

if has_good_credit and not has_no_criminal_record:
    print("Eligible for a loan")

#------------------------Comparison Operators----------------------

temperature = 35

if temperature > 30:
    print("It's a hot day!")
else:
    print("It's not a hot day!")

name = input(" ")
if len(name) < 3:
    print("Name must be at least three characters!")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters!")

else:
    print("Name looks good")

weight = int(input(" weight: "))
unit = input( "(L)s or (K)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"Your weight is {converted} kg")
else:
    converted = weight/ 0.45
    print(f"Your weight is {converted} lb")

weight = int(input("What is your weight?: "))
unit = input(" (l)bsor (k)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"Your weight is {converted} kilogram")
else:
    converted = weight / 0.45
    print(f"Your weight is {converted} pounds")

#-----------------------------While Loop--------------------

i = 1
while i <= 5:
 print("*" * i)
 i = 1 + i
print("Done!")

# ------------------ Guessing Game ----------------------


#Secret_number = 9
#Guess_count = 0
#Guess_limit = 3 

#while Guess_count < Guess_limit:
    #Guess = int(input("Guess: "))
    #Guess_count += 1
    #if Guess == Secret_number:
        #print (" You Won!")
        #break
#else:
    #print(" Try again! ")


#secret_number = 9
#guess_count = 0
#guess_limit = 3

#while guess_count < guess_limit:
    #guess = int(input("Guess: "))
    #guess_count += 1
    #if guess == secret_number:
        #print("You won!")
#else:
#    print("Try again!")



#  ----------------- Car Game -----------------

command = ""
started = False
while True:
    command = input("> ").lower()
    if command== 'start':
        if started:
            print("Car already started!")
        else:
            started = True    
        print("Car started...Ready to go.")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print("""
Start - To start the car
Stop - To stop the car
Quit - To quit
        """)
    elif command == "quit":
        break

    else:
        print ("Sorry, I don't understand that!")