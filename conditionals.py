def f(x):
    print("A", end=" ")
    if (x == 0):
        print("B", end=" ")
        print("C", end=" ")
    print("D")


#Conditional execution: code will only execute if your condition is met
if A and B:
    print("Try a smoothie")
else:
    print("What about strawberries?")

print("goodbye")  #this will always happen, regardless if A and B are True
