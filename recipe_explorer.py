recipe1 = ('Mashed Potatoes', 'American', 30, 'medium')
recipe2 = ('Zeera Aloo', 'Pakistani', 20, 'easy')

print('Recipe 1: ', recipe1[0])
print('Recipe Nationality: ', recipe1[1])
print('Time Taken: ', recipe1[2])
print('Difficulty: ', recipe1[3])\

combined_recipe = (recipe1, recipe2)
print(combined_recipe[0][3])

print(recipe1[1:4])

for x in recipe2:
    print(x)

recipe1_ingredients = {'potato', 'butter', 'salt', 'pepper', 'potato'}
recipe2_ingredients = {'potato', 'Zeera', 'oil', 'paprika', 'Curry Leaf', 'pepper'}

print(recipe1_ingredients)
print(len(recipe1_ingredients))

recipe1_ingredients.add('parsley')
recipe2_ingredients.discard('pepper')

print(recipe1_ingredients,f'\n{recipe2_ingredients}')
