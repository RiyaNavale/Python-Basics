x='Good Morning'
y=' Riya'


# print(f" {x} {y}")

#print(x+y)

#Slicing

#[start:end:step]
print(x[2:])

z='Riya Navale'

print(z[3:9:1])
print(z[-4:-1])

#String Functions

#1) find length
print(len(x))

#2) capitalizing (it only capitalizes the first letter)
name='BOB blue'
print(name.capitalize())

#3) ends with
print(name.endswith("blue"))
print(name.endswith("bob"))

#4) count
fav_color='Pink is my favorite color'
print(fav_color.count('o'))
print(fav_color.count('z'))

#5) find
next_story='Snow white had 7 little dwarfs'
print(next_story.find('7'))
print(next_story.find('had'))
print(next_story.find('hay'))

#6) replace
fav_food=" My favorite food is Pizza"
print(fav_food.replace('Pizza' ,'rice and dal'))
print(fav_food)
fav_food=fav_food.replace('Pizza', 'rice and dal')
print(fav_food)






