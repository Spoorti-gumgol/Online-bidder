import os
from online_bidder_art import logo 
#HINT: You can call clear() to clear the output in the console.

print(logo)


bidder = {}

def adding_bidder(nm, pri):
    bidder[nm] = pri

g = "yes"
while g == "yes":
    name = input("What is the name of the bidder: \n")
    price = int(input("Enter bid price: \n"))
    adding_bidder(name, price)
    g = input("Are there any more bidders:  \n").lower()
    os.system('cls')
   

min = 0
for i in bidder:
    max = bidder[i]
    if max > min:
        min = max
        fin_name = i
print(f"The winner of this bid is {fin_name} with the bid of {min}$")



