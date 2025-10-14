"""thought 7kyu would be more... 
but requires it to be a filled square rather 
than an empty outline ala 
    +++
    +++
    +++
"""
def generate_shape(n):
    # +++\n+++\n+++
    output = ""
    for i in range(n):
        output += "+"*n
        if i != n-1: 
            output += "\n"
    return output

print(generate_shape(3))


# return '\n'.join('+' * integer for i in range(integer))
