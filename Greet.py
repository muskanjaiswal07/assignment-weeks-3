greeting = input("Enter a message: ")
greeting = greeting.lower()

if greeting.startswith("hello"):          
    output = 0
elif greeting[0] == 'h':  
    output = 20
else:                           
    output = 100      

print("Output: $", output)
