# Output Validator
# Made in VSC on Ubuntu Focal Fossa :)
# By Lior
# December 2021

import subprocess

class OutputValidator:
    # Function to replace int global value in main.c
    # Takes the requested value as argument
    def value_replace(value):
        # Read in the file
        with open('main.c', 'r') as file :
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace('__VALUE__', value)

        # Write the file out again
        with open('main.c', 'w') as file:
            file.write(filedata)
    
    # Replace ​ __value__​ in the provided C file with some value
    value_replace('123')

    # Compile the modified file with gcc and create an executable
    subprocess.run(["gcc", "-o", "main.out", "main.c"])

    # Run the executable and get the returned value of the function
    return_value = subprocess.run("./main.out")

    # Check that the return value is the same as you provided
    if return_value.returncode == 123:
        print("output validated")
    else:
        print("output not validated")