import time

#catching all the true falses 
true = ["T", "t", "True"]
false = ["F", "f", "False"]

#storing the correct answers 
correct = 0 

#storing user's name
name = input("What's your name?")

#saying hello to our user and giving them time to read
print("\nOk, " + name +", lets get started. Remember, the following answers are only True or False")
time.sleep(2)

print("\nParis is the capital of France.")
choice = input(">>> ")
if choice in true: 
    #if our user is correct, we'll give em a point, same 
    #with the other if else's 
    correct += 1 

print("\nEngland is an island.")
choice = input(">>> ")
if choice in false: 
    correct += 1

print("\nNorthern Ireland isn't part of Great Britian")
choice = input(">>> ")
if choice in false: 
    correct += 1

print("\nAndorra is between France and Spain.") 
choice = input(">>> ")
if choice in true: 
    correct += 1

print("\nIran use to be a part of the Perisan Empire.")
choice = input(">>> ")
if choice in true:
    correct += 1

print("\nTurkmenistan isn't a real country.")
choice = input(">>> ")
if choice in false:
    correct += 1

print ("\nYou're finished, " + name +". You got", correct, "out of 6 correct.")
