#  "Welcome to OCloud Web Services."

#  example_func
#  Output:
#  a: 2
#  b: 1
#  c: 2
#  d: 0
#  ...

#  - Must output in alphabetical order.
#  - Must output ALL letters, even if they don't appear in the string.
#  - 'A' === 'a', 'B' === 'b', etc.
#  """

# O(1 + (1*n) + 1)
# O(n) where n = len(input)
def count_letters(input: str):
    # create a hashmap of all the letters in alphabet
    letters = "abcdefghijklmnopqrstuvwxyz"
    letterMap: dict = {}
    # O(1 * n)
    for letter in input.lower():
        if letter.is_alpha():
            continue
        letterMap[letter] = letterMap.getOrDefault(letter, 0) + 1

    # O(1)
    for letter in letters:
        if letter in letterMap:
            print("{}:{}".format(letter, letterMap[letter]))
        else:
            print("{}:{}".format(letter, 0))


# After optmizing the algorithm
# HashMaps do not guarantee order!
def count_letters_optimized(input: str):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letterMap = {}

    # O(1 * n)
    for letter in input.lower():
        if letter in letterMap:
            letterMap[letter] += 1
        else:
            letterMap[letter] = 1

    # O(1)
    for letter in letters:
        if letter in letterMap:
            print("{}:{}".format(letter, letterMap[letter]))
        else:
            print("{}:{}".format(letter, 0))


count_letters("Welcome to Amazon Web Services.")

"""
asifoishg -> 21987548678457283497

HashMap(7)

0: []
1: [{947436789436984376: "Python"}]
2: []
3: [{47593759847593: "TypeScript"} -> {8375892765894: "Golang"}]
4: []
5: []
6: []
7: [{84759843768943678: "Java"}]

PUT "Maurice" "TypeScript"
HASH("Maurice") = 47593759847593 % 7 = 3

PUT "Nick" "Golang" = 8375892765894 % 7 = 3

GET "Nick"

1 % 7   = 1
2 % 7   = 2
3 % 7   = 3
4 % 7   = 4
5 % 7   = 5
6 % 7   = 6
7 % 7   = 0
8 % 7   = 1
9 % 7   = 2
10 % 7  = 3

"""