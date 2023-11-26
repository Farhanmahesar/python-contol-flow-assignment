number = int(input("Enter a num: "))
if number > 1:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print("The num is not a prime number")
            break
    else:
        print("The num is a prime number")
else:
    print("The num is not a prime number")