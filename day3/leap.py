#Program to check whether a year is Leap Year


year = int(input())

if (year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)):
    print("leap")
else:
    print("not leap")