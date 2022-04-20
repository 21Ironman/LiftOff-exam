n = input()
is_divisble_by3 = int(n)%3 == 0
is_divisble_by5 = int(n)%5 == 0
if is_divisble_by3 and is_divisble_by5:
    print("FizzBuzz")
elif is_divisble_by3:
    print("Fizz")
elif is_divisble_by5:
    print("Buzz")
else:
    print(n)