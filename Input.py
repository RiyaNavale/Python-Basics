score=int(input("Enter the grade you got on your test"))

if score>=90:
    grade="A"
elif score>+80:
    grade="B"
elif score>+70:
    grade="C"
else:
    grade="F"
print(f"You got an {grade}")
print('-----------------------')

age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")
print('-------------------------')

color=input("Enter in a color:")

if color in ['Blue','blue','Red','red','Yellow','yellow']:
    print("You have selected one of the primary colors")
else:
    print("The color you chose is pretty")
print('------------------------------------------------------')

temperature=float(input("Enter in the current temperature in degrees Celsius"))

if temperature>30:
    print("Be careful, It is very hot outside!")
elif temperature<0:
    print("Be careful, It is very cold outside!")
else:
    print("The temperature is normal")
print('----------------------------------------------')

month=input("Enter the month:").lower()

if month in ['january','february','december']:
    print("The season is Winter")
elif month in ['march','april','may']:
    print("The season is Spring")
elif month in ['june','july','august']:
    print("The season is Summer")
elif month in ['september','october','november']:
    print("The season is Fall")
else:
    print("Enter in a month")
print('--------------------------------------------')

speed_check=float(input("Enter your driving speed in km/h:"))

if speed_check<+60:
    print("Good Job, you are within the speed limit.")
elif speed_check>60 and speed_check<=80:
    print("Be careful, you are slighlty over the speed limit.")
else:
    print("Please slow down, you are over the speed limit.")



    
