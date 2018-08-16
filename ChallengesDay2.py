# LEAP YEAR PROBLEM #
def leap_year(yfromnow):
    ans = (yfromnow*4)+2020
    print(ans)

#leap_year(5613)



#year = int(input("Year? "))

def last_leap_year(year):
    if year<1581:
        print("Syntax not valid")
    elif (year%4) == 0:
        print("This is a leap year")
    elif (year%4) == 1:
        print("Last leap year was " + str(year-1) + ", 1 year ago")
    elif (year%4) == 2:
        print("Last leap year was " + str(year-2) + ", 2 years ago")
    elif (year%4) == 3:
        print("Last leap year was " + str(year-3) + ", 3 years ago")
    elif year<1581:
        print("Please enter a number higher than 1581")

#last_leap_year(year)


# GUESSING GAME #
import random
def guessing_game():
    num = random.randint(0,100)
    guess = int(input("Choose a number from 0 to 100 "))

    if num>guess:
        print("Your guess is too low! The corect answer is " + str(num))
    elif num<guess:
        print("Your guess is too high! The correct aswer is " + str(num))
    elif num==guess:
        print("Amazing! you guessed the number!")
#guessing_game()        
    
# FOREVER RUNNING PROGRAM #
def forever():
    while True:
        print("Hi")

#you can exit the program by holding ctrl+c


# NUMBER PRINTING #

def num_print(jump):
    jump = int(input("Jumps between numbers - "))
    i = 0
    while i < 100:
        print(i)
        i+=jump
#num_print(jump)

# FUN WITH TURTLES #

import turtle
# turtle.color("blue")  #changing the line color
# turtle.penup()
# turtle.pendown()
# turtle.goto(100,200)
# turtle.circle(100)    #drawing a circle

# FACTORIAL #
def factor():
    num = int(input("choose a nubmer to factor "))
    ans = 1
    while num>0:
        ans=ans*num
        print(ans)
        num -=1
    print(ans)

#factor()

# INFORMATION #
colorvar = input("What`s your favorite color? ")
heightvar= input("How tall are you? (Meter.cm)")
hairColorVar = input("What`s your hair color? ")

