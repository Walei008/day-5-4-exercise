#Write your code below this row 👇

for number in range (1,101):
  if number%3==0:
    print(number)
    print("fizz")
  if number%5==0:
    print(number)
    print("buzz")
  if number%3==0 and number%5==0:
    print(number)
    print("fizzbuzz")
  else:
    print(number)