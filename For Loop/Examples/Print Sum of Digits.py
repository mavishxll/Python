### Print sum of digits of a number input by user ###

n = int(input("Enter a number: "))

# Define a function for calculating sum of digits
def SumOfDigits(n): 
    sum = 0 # let sum = 0
    for digit in str(n): # Convert number into string for counting digits
      sum += int(digit)       
    return sum

print(SumOfDigits(n))