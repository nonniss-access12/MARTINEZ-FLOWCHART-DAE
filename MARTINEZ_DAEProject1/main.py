import random

userContinue = True

poultryCategories = [ 
    "Eggs",
    "Food/Feed",
    "Chicken",
    "Turkey"
 ]

eggsTips = [
    "Clean egg shells using a dry cleaning method such as fine sandpaper, a brush or emery cloth.",
    "Collect or pick eggs two to three times a day."
    "Eggs should always be stored pointy end down. This keeps the air sac at the top of the egg, and it keeps the yolk centered and prevents bacteria from entering the yolk."
    "Chicken and Turkey eggs are very different. Both the shell itself and the membrane that separates the egg from the shell are thicker in turkey eggs, making them slightly harder to crack. Turkey eggs are somewhat richer than chicken eggs, with almost twice the calories, protein and fat, despite being just 50 percent larger from chicken eggs."
]

foodorfeedTips = [
    "Choose feed with ideal nutrition for your flock's life stages. For example, for a new born or a several-week-old chick, you will feed them a starter grower. These include crumbled or crushed up grains. Whereas for adult birds, you will feed them their usual pellets. ",
    "Turkeys generally require higher protein levels than chickens, especially during their early growth stages. Their feed may contain up to 28% protein. ",
    "Chickens typically require slightly lower protein levels than turkeys, their feed ranges from 18% to 23% dpending on the growth stage."
    "You don't have to require feeding your birds with store-brought feed. You can raise your birds by feeding them grass, garden scraps such as: lettuce, tomatoes, sweet corn, summer squash, and so on, and at most times, little pebbles or rocks" 
]

chickenTips = [
    "Provide a dust bath “spa” for your hens, (roosters too!) is important to sustain healthy skin and feathers for your birds. The dust bath can be an area of dry dirt or dry sand where your flock has round the clock access to dig and “bathe” feathers and skin."
    "Chicken look great",
    "Chicken are fantastic"
]

turkeyTips = [
    "Same with chickens, Turkeys also use dust baths to sustain healthy skin and feathers. The dust bath can be an area of dry dirt or dry sand where your flock has round the clock access to dig and “bathe"
    "Turkey look great",
    "Turkey are fantastic"
]

# This is a function that display an intro message to the users
def intro():
    print( "Hello! This program will give you free, useful, and personalized tips to help you take care of your birds!" )
    print( "These are the categories you may choose. Please type the number of the selected choice: " )

intro()

number = 1
for category in poultryCategories:
    print( number, category )
    number = number + 1


while userContinue:
    userChoice = int( input( "Please select a choice that is listed above, Type the number of the choice you desire for an easier user experience" ) )

    if userChoice == 1:
        print( eggsTips[ random.randint(0,2) ] )
    elif userChoice == 2:
        print( foodorfeedTips[ random.randint(0,2) ] )
    elif userChoice == 3:
        print( chickenTips[ random.randint(0,2) ] )
    elif userChoice == 4:
        print( turkeyTips[ random.randint(0,2) ] )

    userAnswer = input( "Another tip? Type (Y) for Yes, or (N) for No, for an easier user experience Y/N: " )
    if userAnswer != "Y":
        userContinue = False

# This message is thanking user for using the program
print( "Thank you so much for using the program! Can't wait to see you next time!" )



