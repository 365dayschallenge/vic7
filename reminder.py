
# Get input number

# input = input("Enter a number")


input = 1234567

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
def sumProduct(sum, input):
    numbers = tolist(input)
    for i,y in zip(numbers,magicNumber): 
        sum = sum + (i*y) 
            
    if sum != input%13:
            print(sum)
            sumProduct(0, sum)
    else: print(sum)
sumProduct(sum, input)
