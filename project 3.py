# currency converter
# here we will read the file named (currency.txt) where we have saved  different currencies , 
with open ("currency.txt", "r") as f:
    lines = f.readlines() # readline is used to read the lines 

# here we are going to create dictionary for currencies
currencydict={}
for line in lines:
    parsed= line.split("\t") #used to parse content from files and check if the values meet your testing criteria
    currencydict[parsed[0]]= parsed[1]
# print(currencydict)


amount = int(input("enter amount"))

print("which of the currency you want to convert")
[print( item ) for  item in currencydict.keys()]

currency= input("enter the currency name you want to find: : ")
print(f"{amount} pkr is equal to {amount *float(currencydict[currency])} {currency}") #thos is basically a formula for converting currency