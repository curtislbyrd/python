# Ask for user input
input_string = input("Enter a string: ")

# Convert input to a string
if not isinstance(input_string, str):
    input_string = str(input_string)

# Reverse the string
reversed_string = input_string[::-1]

print("The reversed string is:", reversed_string)