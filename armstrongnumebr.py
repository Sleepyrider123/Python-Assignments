number = input('Input a number: ')
sum = 0
for count in number:
    count = int(count)
    power = len(number)

    sum += count**power

if number == str(sum):
    print(f'{number} is an armstrong number')
else:
    print(f'{number} is not an armstrong number')

    