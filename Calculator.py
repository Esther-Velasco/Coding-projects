
"""
Lesson on fuctions with outputs
IMPORTANT. WE TRIGGER A FUNCTION WHEN WE USE THE PARENTHESIS :   def function_aqui (n1, n2)
If we simply want to store the function inside a variable, we can simply write the variable name :
    
pepito = function_aqui
Then call that function stored in a variable using the variablename:
    pepito(n1:3, n2:4)


For use case bellow:
there is also the function .capitalize()

def format_name(f_name,l_name):
    capitalized_name = f_name.title()
    capitalized_lastname = l_name.title()
    
    return capitalized_name + " " + capitalized_lastname
    

#calling the function using two parameters: f_name and l_name

format_name(input("what is your name?"), input("what is your last name?"))

def is_leap_year (year):
    '''docstrings will have to come here explaining our function'''
    if year % 4 != 0:
        return bool(False)
    
    elif year % 100 != 0:
        return bool(True)
    
    elif year % 400 != 0:
        return bool(False)
    
    else:
        return bool(True)
    
    
is_leap_year(2024)



"""

#calculator project

def add(n1, n2):
    return n1 + n2

""" to do: create substract, multiply and divide"""

def substract(n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2
    
""" to do: create a dictionary with keys +, *, -, /, and values the functions. Remember we do not use the parenthesis in the functions since we are not calling them but defining them in a dictionary"""

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
    }

""" to do: use dictionary operations to perform a calculation. Multiply 4*8 using the dictionary. """

def run_calculator():
    
    accumulation = True
    first_number = float(input("What is the first number?: "))
   
    while accumulation:
        for key in operations:
            print(key)
        chose_operation = str(input("Pick an operation: "))
        second_number = float(input("What is the second number?: "))
    
        result = operations[chose_operation](first_number,second_number)
        print(f'{first_number} {chose_operation} {second_number} = {result}')
        
        continue_playing = str(input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")).lower()
        
        if continue_playing == 'y':
            first_number = result
        
        else:
            accumulation == False
            print("\n" * 20)
            run_calculator()

run_calculator()