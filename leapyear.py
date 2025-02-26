year = int(input("enter the year :"))
if year%100==0 and year%400 !=0:
    print("this is not leap year")
elif year%100!=0 and year%4==0:
    print("this is a leap year")
else:
    print("this year is not leap year")