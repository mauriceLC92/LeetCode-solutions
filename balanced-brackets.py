"""

 	()								= TRUE
 	(1 + 2) * 4 			= TRUE
 	((2 + 4)					= FALSE
 	)(								= FALSE
 	(2 / 3) * (2 - 1)	= TRUE
  (1 * 3 + (7 - 2)) = TRUE
 	()(								= FALSE
 

[')', '(']
"""


def balanced_brackets(inputStr):
    bracket_counter = 0

    for letter in inputStr:
        if letter == "(":
            bracket_counter += 1
        elif letter == ")":
            bracket_counter -= 1

        if bracket_counter < 0:
            return False

    return bracket_counter == 0


print(balanced_brackets(")("))  # False
print(balanced_brackets("((2 + 4)"))  # False
print(balanced_brackets("(2 / 3) * (2 - 1)"))  # True
