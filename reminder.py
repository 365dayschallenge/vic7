import sys
# Get input number

input = input("Enter a number: ")

# convert input to list
def tolist(input):
    digit_string = str(input)
    digit_map = map(int, digit_string)
    numbers = list(digit_map)
    return numbers[::-1]

numbers = tolist(input)
n = len(numbers)


#get magicnumber 
def getmagicNumber():
    lst = range(0,n,1)
    magicNumber =[]
    for y in lst : 
        z=pow(10,y)
        x = z % 13
        magicNumber.append(x)
    return(magicNumber)
magicNumber = getmagicNumber()

sum=0

# sum the multiplications
def thirt(sum, input):
    numbers = tolist(input)
    for i,y in zip(numbers,magicNumber): 
        sum = sum + (i*y) 
            
    while sum%13 == input%13:  
        numbers = tolist(sum) 
        sum = 0  
        for i,y in zip(numbers,magicNumber):
            sum = sum + (i*y) 
        print(sum)
        sys.exit()

thirt(sum, input)
