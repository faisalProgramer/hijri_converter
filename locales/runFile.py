from hijri_converter import convert

print("Enter h to convert to Hijri, or press g to convert to Gregorian?")
typeOfconv= input()
if typeOfconv == "g" or typeOfconv == "G":
    print("Enter the Hijri date in year")
    y = int(input())
    print("Enter the Hijri date in month")
    m = int(input())
    print("Enter the Hijri date in day")
    d = int(input())
    # Convert a Hijri date to Gregorian
    Gregorian_date = convert.Hijri(y, m, d).to_gregorian()
    print(Gregorian_date)

elif typeOfconv =="h"or typeOfconv == "H":
    print("Enter the Gregorian date in year")
    y = int(input())
    print("Enter the Gregorian date in month")
    m = int(input())
    print("Enter the Gregorian date in day")
    d = int(input())
    # Convert a Gregorian date to Hijri
    Hijri_date = convert.Gregorian(y, m, d).to_hijri()
    print(Hijri_date)
else:
    print("invalid input")