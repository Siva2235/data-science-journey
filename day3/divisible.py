#Program to check whether a number is Divisible by 5 and 11


nums = int(input())

if (nums % 5 == 0 and nums % 11 == 0):
    print("Divisible by 5 and 11")
else:
    print("Not Divisible by 5 and 11")