# Joseph Griffith
# G00350112
# Graph Theory Project 
# Shunting Yard Algorithm To Convert Regular Expressions from infix to postfix



# Argument containing a infix regular exspression
def shunt(infix):

    # Precedence given to the regular exspression using a python dictionary
    specials = {'*': 50, '.': 40, '|': 30 }

    # Postfix regular exspression and stack is where the operators will be pushed and poped. 
    pofix = ""
    stack = ""


    # Shunting Yard Algorithm
    for c in infix:
        if c == '(':
            stack = stack + c
        
        # Takes what is on the end of the stack and place it into pofix and then 
        # remove it from the stack and finally it removes the '(' from the stack
        elif c == ')':
            while stack[-1] != '(': 
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack[:-1]

        # Takes what is on the end of the stack and place it into pofix and then remove
        #  it from the stack and then places the special character onto the stack
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack + c
            
        else:
            pofix = pofix + c

    # Takes what is on the end of the stack and place it into pofix and then remove it from the stack
    while stack:
        pofix, stack = pofix + stack[-1], stack[:-1]
        




    return pofix



