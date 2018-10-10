# Create function for calculation.
def Calculate():
    # Create input to ask user what type of math operation he would like to complete.
    operator = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ** for power
    % for modulo
''')

    # Store user input into variables.
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))

    # Check user input and use correct math operation.
    if operator == '+':
        print('{} + {} ='.format(x, y), (x + y))
    elif operator == '-':
        print('{} - {} ='.format(x, y), (x - y))
    elif operator == '*':
        print('{} * {} ='.format(x, y), (x * y))
    elif operator == '/':
        print('{} / {} ='.format(x, y), (x / y))
    elif operator == '**':
        print('{} ** {} ='.format(x, y), (x ** y))
    elif operator == '%':
        print('{} % {} ='.format(x, y), (x % y))
    else:
        print('Use a valid operator')

    # Call function to request new calculation.
    calculateAgain()

# Create function to request for new calculation.
def calculateAgain():

    # Create input to ask user if he wants to make a new calculatoin or exit.
    calc_again = input('''
    Do you want to make a new calculation?
    Press Y for YES or N for NO.
''')

# Check user input and continue or exit.
    if calc_again.upper() == 'Y':
        Calculate()
    elif calc_again.upper() == 'N':
        print('Shutting off')
    else:
        calculateAgain()

# Call function to make calculation.
Calculate()
