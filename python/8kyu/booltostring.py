# Convert a boolean to a string
def boolean_to_string(b):
    if b == True:
        return "True"
    else:
        return "False"

# can be condensed into a simple return
def alt_boolean_to_string(b):
    return 'True' if b else 'false'

# can use str to convert type 
def alt2_boolean_to_string(b):
    return str(b)

print(boolean_to_string(False))
     
