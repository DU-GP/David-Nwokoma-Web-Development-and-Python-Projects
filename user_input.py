name = input("What is your name?: ")
age = input("How old are you?: ")
location = input("Where do you live?: ")
print("Hello!, " + name + " you are " + age + " old, " + " you live at " + location)



#Lists and Tuples
N1 = []

N2 =[1, "Hello", 2.8]
print(N2)


n3 = ['p','r', 'o', 'g', 'r', 'a', 'm' ]
print(n3[2:5])

n3.append('m')
print(n3)
N2.extend(n3)
print(N2)