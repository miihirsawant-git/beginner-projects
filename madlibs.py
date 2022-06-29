# Madlibs Game
"""
Pseudo Run
    Define a variable
        res = "freeCodeCamp: Kylie Ying"
    
    Three ways to concatenate strings
        1.  Direct concatenate with a plus sign 
           print("Using resource " + res)
        2.  Concatenate by calling a string.format function for variable
            print("Using resource {}".format(res))
        3.  Concatenate by prepending an f string 
            print(f"Using resource {res}")
    
    Print strings
"""

#   Plot: Kids pizza pizza funny madlibs (https://i.pinimg.com/564x/cc/0c/58/cc0c582acfb8853afcfb0af8aa33184d.jpg)

#   #   Use of the third way of concatenation
#   #   Use of split function to accept multiple entries from user
noun1, noun2 = input("Enter two nouns: ").split()
adj1, adj2, adj3, adj4 = input("Enter four adjectives: ").split()
num1, num2 = input("Enter two number: ").split()
food1, food2 = input("Enter two types of food: ").split()

#   #   Traditional single input entry from user
noun3 = input("Enter a cooking utensil: ")
nationality = input("Enter a nationality: ")
name1 = input("Enter a name: ")
pluralnoun = input("Enter a plural noun: ")
shape = input("Enter a shape in plural: ")

#   #   Madlibs game function
madlib = f"\n\nPizza Pizza Madlibs \n\nPizza was invented by a(n) {adj1} {nationality} chef named {name1}. To make a pizza, \
you need a lump of {noun1}, and make it into thin, round {adj2} {noun2}. Then you cover it \
with {adj3} sauce, {adj4} cheese, and fresh chopped {pluralnoun}. Next you have to \
bake it in a very hot {noun3}. When it's done, cut it into {num1} {shape}. Some \
kids like the {food1} pizza, but my favorite is {food2} pizza. If I could, \
I could eat {num2} times a day!\n\n"

#   #   Print the game
print(madlib)