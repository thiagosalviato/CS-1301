from datetime import date
myDate = date.today()
myDateAsString = str(myDate)
print("Today's date: " + myDateAsString)

myDateAsString = str(date.today())
print("Today's date: " + myDateAsString)

myDate = date.today()
print("Today's date: " + str(myDate))

print("Today's date: " + str(date.today()))

print("Today's date:", date.today())