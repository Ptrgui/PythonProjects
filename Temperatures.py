# This code transforms temperatures of Kelvin, Celsius and Fahrenheit

# Conversion between Celsius and Kelvin
# Celsius to Kelvin:  K = C + 273.15
# Kelvin to Celsius: C = K - 273.15

# Conversion between Fahrenheit and Celsius
# Fahrenheit to Celsius: C = (F - 32) * 5/9
# Celsius to Fahrenheit: F = C*(9/5) + 32

# Conversiontemp between Fahrenheit and Kelvin
# Fahrenheit to Kelvin: K = (F - 32) * 5/9 + 273.15
# Kelvin to Fahrenheit: F = (K-273.15) * 9/5 + 32




def f_to_c():
        # Fahrenheit to Celsius
        F = float(input('Please enter a value for Fahrenheit: '))
        C = F - 32 * 0.55
        print('The temperature in Celsius is: ', C)

def c_to_f():
        #Celsius to Fahrenheit
        C = int(input('Please enter a value for Celsius: '))
        F = C * 1.8 + 32
        print('The temperature in Fahrenheit is :', F)

def c_to_k():
        # Celsius to Kelvin
        C = int(input('Please enter a value for Celsius: '))
        K = C + 273.15
        print('The temperature in Kelvin is: ', K)

def k_to_c():
        #Kelvin to Celsius
        K = int(input('Please enter a value for Kelvin: '))
        C = K - 273.15
        print('The temperature in Celsius is: ', C)

def f_to_k():
        #Fahrenheit to Kelvin
        F = int(input('Please enter the value for Fahrenheit: '))
        K = (F - 32) * 0.55 + 273.15
        print('The temperature in Kelvin is: ', K)

def k_to_f():
        #Kelvin to Fahrenheit
        K = int(input('Please enter a value for Kelvin: '))
        F = (K - 273.15) * 1.8 + 32
        print('The temperature in Fahrenheit is: ', F)

def errorquit():
        quit()



print('1 - Fahrenheit to Celsius\n'
      '2 - Celsius to Fahrenheit\n'
      '3 - Celsius to Kelvin\n'
      '4 - Kelvin to Celsius\n'
      '5 - Fahrenheit to Kelvin\n'
      '6 - Kelvin to Fahrenheit\n'
      '0 - Exit\n')

choice = int(input('Please choose the conversion option: \n'))

#Creating a dictionary
operations = {
    1:f_to_c,
    2:c_to_f,
    3:c_to_k,
    4:k_to_c,
    5:f_to_k,
    6:k_to_f,
    0:errorquit
}

output = operations.get(choice, errorquit)()
print(output)

