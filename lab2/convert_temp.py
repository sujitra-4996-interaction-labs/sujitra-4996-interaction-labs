correct_input=False
while not correct_input:
    try:
        temp_cel=float(input("Enter a temperature in Celsius: "))
        temp_fah=(9/5)*temp_cel+32
        print(f"{temp_cel:.2f} in celsius is {temp_fah:.2f} fahrenheit")
    except ValueError:
        print('Please enter a valid flooating point for the temperature')
    else:
        correct_input = True