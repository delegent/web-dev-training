# While loops in python
"""initialization
condition
updation""
i = 1
while i <= 10:
    print(f'Hello {i}')
    i += 1"""

# Fizz Buzz Problem
"""30
1  2 3 4 5 6 ...30
divisible by 3 -> Fizz
divisible by 5 -> Buzz
divisible by 3 and 5 both -> FizzBuzz
"""
no = int(input("Enter a number "))
i = 1
while i <= no:
    if(i % 3 ==0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)
    i += 1;
