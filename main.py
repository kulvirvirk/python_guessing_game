# 1. get user input about their favorite food. 
# 2. if user enter the name of your favorite food, say "Yep! so amazing!"
# 3. if user enter some other, say "Yuck! that's not it!"
# 4. say thanks at the end

my_fav_food = 'chicken'
user_fav_food = input("What's my favorite food: ")

if my_fav_food == user_fav_food:
  print('Yep! so amazing!')
else:
  print("Yuck! that's not it!")

print('Thanks for playing the Guessing Game, Bye!')