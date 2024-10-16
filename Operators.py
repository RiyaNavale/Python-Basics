print('\n------Operators------\n')

print('\n----Arithmetic Operators----\n')

print(12+33)
print(125-97)
print(8*12)
print(45/5)
print(2**2)
print(7%2)

print('\n----Comparison Operators----\n')
a=17
b=5

if a>5:
    print("This comparison is true")
else:
    print("This comparison is false")

if a<5:
    print("This comparison is true")
else:
    print("This comparison is false")

if a>=5:
    print("This comparison is true")
else:
    print("This comparison is false")

if a<=5:
    print("This comparison is true")
else:
    print("This comparison is false")

if a==5:
    print("This comparison is true")
else:
    print("This comparison is false")
if a!=5:
    print("This comparison is true")
else:
    print("This comparison is false")

print('\n----Logical Operators----\n')

a=False
b=True
result=a and b
print(result)

a=False
b=True
result=a or b
print(result)

a=False
result=not a
print(result)

age=12
is_student=False

if age<30 and is_student:
    print("You qualify for a student discount.")
else:
    print("You aren't a student.")

light_color="red"
pedestrian_waiting=False

if light_color=="red" and not pedestrian_waiting:
    print("Stop")
else:
    print("You can go")

username="Powder Puff"
password=True

if username=="Powder Puff" and password:
    print("Access granted")
else:
    print("Access denied.")
