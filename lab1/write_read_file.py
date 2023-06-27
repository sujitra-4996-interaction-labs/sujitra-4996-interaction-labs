number1=input('Enter a number:')
number2=input('Enter a number:')
number3=float(number1)+float(number2)
txt=(f'{number1} + {number2} = {number3}')
print(txt)
print('Writing to file number.txt')
with open('number.txt', 'w') as nbfile:
    nbfile.write(txt)
print('Reading from file number.txt')
with open('number.txt', 'r') as nbfile:
    readfile=nbfile.read()
    print(readfile)