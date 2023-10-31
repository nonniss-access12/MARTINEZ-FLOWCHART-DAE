import random

userContinue = True

poultryCategories = [ 
    "Eggs",
    "Food",
    "Chicken",
    "Turkey"
 ]

eggsTips = [
    "Eggs are tasty",
    "Eggs look great",
    "Eggs are fantastic"
]

foodTips = [
    "Food are tasty",
    "Food look great",
    "Food are fantastic"
]

chickenTips = [
    "Chicken are tasty",
    "Chicken look great",
    "Chicken are fantastic"
]

turkeyTips = [
    "Turkey are tasty",
    "Turkey look great",
    "Turkey are fantastic"
]

# This is a function that display an intro message to the users
def intro():
    print( "Hello, this program ...." )
    print( "These are the categories. Please select a choice: " )

intro()

number = 1
for category in poultryCategories:
    print( number, category )
    number = number + 1


while userContinue:
    userChoice = int( input( "Please select a choice: " ) )

    if userChoice == 1:
        print( eggsTips[ random.randint(0,2) ] )
    elif userChoice == 2:
        print( foodTips[ random.randint(0,2) ] )
    elif userChoice == 3:
        print( chickenTips[ random.randint(0,2) ] )
    elif userChoice == 4:
        print( turkeyTips[ random.randint(0,2) ] )

    userAnswer = input( "Another tip y/n: " )
    if userAnswer != "y":
        userContinue = False

# This message is thanking user for using the program
print( "Thank you for using the program" )



