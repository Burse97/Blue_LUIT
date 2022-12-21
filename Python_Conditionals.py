#!/usrbin/env python3.7

# python implementation goes here 

value = int(input("Enter an interger value: "))

if value % 5 == 0 and value % 3 ==0:
    print("FizzBuzz")
Elif value % 3 == 0:
    print("Fizz")
Elif value % 5 == 0:
    print("Buzz")
    else:
        print(value)