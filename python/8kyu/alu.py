# alu (TM)
# vim commands are such a brain 
def basic_op(operator, value1, value2):
    match operator:
        case '*':
            sum = value1 * value2
        case '/':
            sum = value1 / value2
        case '+':
            sum = value1 + value2
        case '-':
            sum = value1 - value2
    return sum

print(basic_op('-',5,5))

#this is pretty much standard, i fear it makes more 
# sense for it be in a switch, though codewars best voted did it with an if-chain 

# however the eval function is new to me and very clever
#
# def basic_op(operator, value1, value2):
#     return eval("{}{}{}".format(value1, operator, value2))

