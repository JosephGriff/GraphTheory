# Thompson's construction
# Joseph Griffith
# G00350112

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
        self.initial = initial
        self.accept = accept

def compile(profix):
    nfastack = []

    for c in profix:
        if c == '.':
            # Pop two NFA's off the stack.
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            # Connect first NFA's accept state to the second's initial.
            nfa1.accept.edge1 = nfa2.initial
            # Push Nfa to the stack.
            nfastack.append(nfa1.initial, nfa2.accept)