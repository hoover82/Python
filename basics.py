
## ##########################################################
##
##  basics.py
##  Dan Stober, 2018-03-08
##  Demonstration of basic language structures
##
## ##########################################################


# Pound sign is comment character

# Print statement, use parentheses in python 3.x

print("Hello World")

#print blank space
print ()
#String literals may use single quotes OR double quotes

print ('string in single quotes')
print ("string in double quotes")
print ()


#For "if", statement end with colon, (no "then" keyword")
#  indent all statements which are part of the block
#  (Indentation must be identical)

if 1==1:
    print ("The 'if' statement was true")
    print ('This statement is a part of the "if-true" block')
    print ("So is this one")

elif 2==2:
    #Only the very first true block is executed -- elif is optional
    print ("This statement, even though true, will not print")

else:
    
    print ("This statement will be printed only if none of the earlier conditions were true")

print ("This statement is NOT part of the 'if' block; it will print always")

print ("\nSubsequent line")  ##Note: '\n' is new-line character.

#print can handle numbers or strings, but not mixed
print ("\Dallin")
print ( 1.2345)
#print ( "Beiene is number " + 1)

print ("\n")

##################################################################

# Variables do not need to be declared
# Variables given a datatype based on assignment

x = 1
y = 2.786
z = 'Dan'

print (x)
print (y)
print (z)

# Datatypes can change based on new assignment
x = "I'm now a string"
print(x)

print()

# Variable names are case-sensitive.
# (In fact, all elements of python are case sensitive)

Y = "This is not re-assigning a new value to 'y'"
print (y)
print (Y)

print()


city="Beverly Hills"
state = 'CA'
zip=90210

# Concatentation uses "plus" sign
cityState = city + " " + state

print (cityState)

# Cannot concatentate strings and numbers
#cityZip = city + zip   #This statement will raise error

#Must convert number to string first
cityZip = city + str(zip)

print (cityZip)

print ("\n* * * * * * LOOPS * * * * * \n")
#Loops

# Keyword "for" with colon at end

# Range with two numbers  -- between but top number is NOT included
for i in range (1,5):
    print (i)

print ()

# Range, with one number -- assumed the zero is bottom number.
#   Agsin, top number is not included

for i in range (4):
    print (i)

print ()

#Range with three numbers -- third number is "step" value

for i in range (0,10,2):
    print (i)

print ()

# Nested loop
for i in range (3):
    for j in range (10,12):
        print ( str(i) + "×" + str (j) + " = " + str ( i*j))

print ()

#iterating through a list array
for i in [1,2,3,5,7,11,13,17,19,23]:
    print (i)
    
print ()

# Iterating through a string -- each character is a loop
for i in "DAN":
    print (i)

print ()

#Assigning a list array to a variable
primes = [1,2,3,5,7,11,13,17,19,23]

print ( primes)

print()

#Add a value to array

primes.append ( 29)

print (primes)

# Access individual values of array
# Indexed from zero, so primes[0] is first one

print ("primes[0] is first value from array:  " + str ( primes[0]))
print ("primes[4] is fourth value from array: " + str ( primes[4]))

print ()
#Iterate through  the values in an array
for i in primes:
    print (i)

print ()
#iterate through index values of array
for i in range (len(primes)):
    print(i)
    print ("Index is: " + str ( i) + " and value in array position (primes[i]) is: " + str(primes[i]))    

print ()

#Array also can contain strings
    
names = ["Matthew","Mark","Luke","John"]

for i in names:
    print (i)
    
print ()

### DICTIONARY ####
#  Similar to key/value pairs.  
#  Use curly braces. Colon separates key from value; comma separates entries

myDictionary = {1:1, 2:4, 3:9, 4:16, 6:36}

print (myDictionary [4])

print ()

## Keys and/or values can be strings, too
chapters = {"Genesis":50,"Exodus":40,"Leviticus":27,"Numbers":35}

print ("Accessing a dictionary value by referencing its key:")
print (chapters ["Exodus"])

print ()

print ("Iterating through dictionary -- iterator returns keys:")

for i in chapters:
    print (i)

print ()

print ("Iterating through dictionary -- using iterator to get values:")

for i in chapters:
    print ( chapters [i])

### NESTING DICTIONARIES ########
    
print ( "\n\n* * * * * * * * *  NESTING DICTIONARIES * * * * * \n\n")

emps = { "SKLYON":{"givenName":"Steve Lyon","RodneyName":"Stevie Wonder"}
        ,"COLPIERC":{"givenName":"Lee Pierce","RodneyName":"Colonel Pierce"}
        ,"CODSTOBE":{"givenName":"Dan Stober","RodneyName":"Danno"}
        ,"DROGERS2":{"givenName":"Dallin Rogers","RodneyName":"Dallio"}
        ,"KBELL125":{"givenName":"Kyle Bell","RodneyName":"Monsieur Cloche"}
        ,"LACARLIS":{"givenName":"Laura Carlisle"}      ## Note that this one has only one nested entry
        ,"JMAIR":{"givenName":"James Mair","RodneyName":"Jammers"}
        } 

print ( emps ["COLPIERC"]["RodneyName"])

print()

#This one will raise an error because it does not exist
#It's OK if nested dictionaries have differerent keys
#print ( emps ["LACARLIS"]["RodneyName"])

for i in emps:
    for j in emps[i]:
        print ( i + ": " + j + " --> " + emps[i][j])


print ("ALL DONE")

