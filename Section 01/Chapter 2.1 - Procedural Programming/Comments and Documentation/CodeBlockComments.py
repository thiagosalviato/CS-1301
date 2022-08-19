#Countdown function
#Prints the numbers from 1 to i
#on a single line
def countdown(i):
    for j in range(1,i + 1):
        print(j, end = " ")
    print()
countdown(10)
countdown(5)
countdown(2)
