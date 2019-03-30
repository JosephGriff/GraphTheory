# Joseph Griffith
# G00350112
# Graph Theory Project 


# Argument containing a infix regular exspression
def shunt(infix):

    # Precedence given to the regular exspression using a python dictionary
    specials = {'*':50, '+':45, '?':45, '.':40, '|':30}

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
            
        # Appending the c char onto the pofix regular expression
        else:
            pofix = pofix + c

    # Takes what is on the end of the stack and place it into pofix and then remove it from the stack
    while stack:
        pofix, stack = pofix + stack[-1], stack[:-1]
        
    return pofix

# Printing out pofix regular expression
# print(shunt("(a.b)|(c*.d)"))


# Represents a state with two arrows, labelled by label.
# Use None for a label representing "e" arrows.
class state:
    label = None
    edge1 = None
    edge2 = None

# an NFA is represented by its initial and accept states.
class nfa:
    initial = None
    accept = None

    def __init__(self, initial, accept):
        self.initial, self.accept = initial, accept

def compile(profix):
    nfastack = []

    for c in profix:
        # Operator - Concatenate
        if c == '.':
            # Pop two NFA's off the stack.
            nfa2, nfa1 = nfastack.pop(), nfastack.pop()
            # Connect first NFA's accept state to the second's initial.
            nfa1.accept.edge1 = nfa2.initial
            # Push Nfa to the stack.
            newnfa = nfa(nfa1.initial, nfa2.accept)
            nfastack.append(newnfa)

        # Operator - OR 
        elif c == '|':
            # Pop two NFA's off the stack
            nfa2, nfa1 = nfastack.pop(), nfastack.pop()
            # Create a new initial state, connect it to initial states
            # of the two NFA's popped from the stack
            initial, initial.edge1, initial.edge2 = state(), nfa1.initial, nfa2.initial
            # Create new accept state, connecting the accept states 
            # of the two NFA's popped from the stack, to the new state.  
            accept = state()
            nfa1.accept.edge1, nfa2.accept.edge2 = accept, accept
            # Push new NFA to the stack
            newnfa = nfa(initial,accept)
            nfastack.append(newnfa)

        # Operator - 0 or more
        elif c == '*':
            # Pop a single nfa from the stack
            nfa1 = nfastack.pop()
            # Create new initial and accept states
            initial, accept = state(), state()
            # Join the new intial state to nfa1's initial state and the new accept state.
            initial.edge1, initial.edge2 = nfa1.initial, accept
            # Join the old accept state to the new accept state and nfa1's initial state.
            nfa1.accept.edge1, nfa1.accept.edge2 = nfa1.initial, accept
            # Push  new nfa to the stack.
            newnfa = nfa(initial,accept)
            nfastack.append(newnfa)

        # Operator - 1 or more
        elif c == '+':
            #pop single nfa from the stack
            nfa1 = nfastack.pop()
            #create new init and accept state
            initial, accept = state(), state()
            #join new initial state to nfa's initial state and the new accept state
            initial.edge1 = nfa1.initial
            #join the old accept state to the new accept, and nfa1's initial state
            nfa1.accept.edge1, nfa1.accept.edge2 = nfa1.initial, accept
            #push new nfa to stack
            new_nfa = nfa(initial, accept)
            nfastack.append(new_nfa)

        # Operator - 1 or 0
        elif c == "?":
            # pop a single nfa from the stack
            nfa1 = nfastack.pop()
            # create new initial and accept state
            initial, accept = state(), state()
            # point new initial state edge1 to popped nfa's initial state 
            initial.edge1 = nfa1.initial
            # point new initial states edge2 to new accept state
            initial.edge2 = accept
            # point popped nfa's accept state edge1 to new accept state 
            nfa1.accept.edge1 = accept
            # push new nfa to stack
            new_nfa = nfa(initial, accept)
            nfastack.append(new_nfa)
            
        # Handle all non special characters
        else:
            # Create new initial and accept states.
            accept, initial = state(), state()
            # Join the initial state to the accept state using an arrow labelled c.
            initial.label, initial.edge1 = c, accept
            # Push new nfa to the stack
            newnfa = nfa(initial,accept)
            nfastack.append(newnfa)

    # nfastack should only have a single nfa on it at the end of a valid regular expression in postfix notation
    return nfastack.pop()

# print(compile("ab.cd.|"))
# print(compile("aa.*"))

def followes(state):
    """Return the set of states that can be reached from state following e arrows"""
    # Create a new set, with state as its only member.
    states = set()
    states.add(state)

    # Check if state has arrows labelled e from it
    if state.label is None:
        # Check if edge1 is a state
        if state.edge1 is not None:
            # If there's an edge1, follow it.
            states |= followes(state.edge1)
        # Check if edge2 is a state.
        if state.edge2 is not None:
            # If there's an edge2, follow it.
            states |= followes(state.edge2)

    # Return the set of states
    return states

def match(infix, string):
    """ 
        Matches string to the infix regular expression.
        Compiles infix regular expressions to postix then creates NFA's from them.
        Match creates two empty sets of states existingSet and futureSet.
        Then you can loop through a string to find all accesible states from that character in said string. 
    """

    # Shunt and compile regular expression.
    postfix = shunt(infix)
    nfa = compile(postfix)

    # The existingSet set of states and the futureSet set of states.
    existingSet = set()
    futureSet = set()

    # Add initial state to the existingSet set
    existingSet |= followes(nfa.initial)

    # Loop through each character in the string.
    for s in string:
        # Loop through the existingSet set of states.
        for c in existingSet:
            # Check if that state is labbelled s.
            if c.label == s:
                # Add edge1 state to the futureSet set.
                futureSet |= followes(c.edge1)
        # Set existingSet to futureSet, and clear out futureSet.
        existingSet = futureSet
        futureSet = set()

    # Check if the accept state is in the set of existingSet states.
    return(nfa.accept in existingSet)


# Tests
infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*","a.(b.b)*.c","a?c*b", "b+c?a"]
strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

for i in infixes:
    for s in strings:
        print(match(i, s), i, s)


