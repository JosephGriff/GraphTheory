# Joseph Griffith - G00350112 - GraphTheory
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Third year Python project using Thompson's construction and shunting algorithm. 

Project guidelines:

"You must write a program in the Python programming language that can build a non-deterministic finite automaton (NFA) from a regular expression, and can use the NFA to check if the regular expression matches any given string of text. You must write the program from scratch and cannot use the re package from the Python standard library nor any other external library."

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Running the Project

Clone the repository: 

      $ git clone https://github.com/JosephGriff/GraphTheory.git

Change directory:

      $ cd Graph Theory Project
      
Run .py file:

      $ python GTProject.py
      
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Anatomy of Project

The end product of the program consists of 4 functions, which contents are commented for ease of re-usability and understanding.

- Shunt

- Compile

- Followes

- Match


## Shunt

The shunt function takes a regular expression from 'infix' notation to 'postfix' notation.
 
Some examples of this are given in the NFA drawing image in the repository.

## Compile

Compile converts a regular expression into a NFA where it is then used to match given strings against the regular expressions listed.
Compile will parse the postfix and return an NFa for all of the special operators that have been given in the shunting algorithm.

## Followes

Return the set of states that can be reached from state following e arrows.

## Match

Matches string to the infix regular expression.
Compiles infix regular expressions to postix then creates NFA's from them.
Match creates two empty sets of states existingSet and futureSet.
Then you can loop through a string to find all accesible states from that character in said string. 
