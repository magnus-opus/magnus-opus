#members input the fat grams they consume in a day
fat_grams=int(input('The number of fat grams consumed in a day: '))
fat_calories= fat_grams * 9

carbs_grams=int(input('The number of carbohydrate grams consumed in a day: '))
carb_calories=carbs_grams * 4

#total calories consumed.
calories_consumed=fat_calories + carb_calories
print('The number of calories in',fat_grams,'fat grams is:', fat_calories,'cal''\n''The number of calories in',carbs_grams,'carbohydrate grams is:',carb_calories,'cal','\n''The total calories consumed is:',calories_consumed,'cal')
