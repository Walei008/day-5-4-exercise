#Write your code below this row 👇

for number in range (1,101):
  if number%3:
    print(number)
    print("fizz")
  if number%5:
    print(number)
    print("buzz")
  if number%3%5:
    print(number)
    print("fizzbuzz")