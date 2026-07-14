num = int(input("Enter a number: "))

if num > 1:
    for x in range(2,int(num**0.5)+1):
        if num % x == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

