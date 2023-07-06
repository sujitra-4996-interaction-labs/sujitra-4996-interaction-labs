def compute_factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*compute_factorial(n-1)
def main():
    try:
        user_input=int(input('Enter an integer:'))
        if user_input<0:
            print('Please enter a non-negative integer')
            return
        factorial=compute_factorial(user_input)
        print(f'The factorial({user_input}) is {factorial}')
        return
    except ValueError:
        print('Please enter a valid integer')
if __name__ == "__main__":
    main()