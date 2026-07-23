fruits = ['strawberry', 'mango', 'banana', 'dragonfruit', 'peach']

print(len(fruits))

print(fruits[0])

print(fruits[-1])

print(fruits[3])

print(fruits[1:4])

fruits.append('pineapple')
print(fruits)

fruits.remove('banana')
print(fruits)

fruits.sort()
print("After sorting alpha: ", fruits)

fruits.reverse()
print('after reversing:', fruits)


dic = {"name" :"Abdullah", "age": 19, "fave_sub": "Physics"}

print(dic)

print(dic.get('experience'))
dic['experience'] = 7

dic['age'] = 20

print('after changes: ', dic)

dic.pop('fave_sub')
print(dic)



ranking = [1 , 2 , 3 , 4]
hobbies = ['guitar', 'gaming', 'perfumes', 'football']

hobby_rank = dict(zip(ranking, hobbies))

print(hobby_rank)