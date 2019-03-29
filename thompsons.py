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