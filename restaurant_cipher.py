
###########################################################
# Restaurant Cipher                                       #
###########################################################
# Ali always asks his chef to cook some specific recipes. # 
# They wanted to have some fun, so, they agreed to name   #
# some recipes with just the letters: A, B, C, D, E, F    #
# and G, and not more.                                    #
# Now, if Ali wants a recipe, he sends a secret message   #
# to his chef that asks for a single recipe.              #
#                                                         #
# Your task is to break Ali's scheme for creating the     #
# secret messages, based on the example messages in       #
# the testcase below.                                     #
#                                                         #
###########################################################


letter_count_proto = {
    "A" : 0,
    "B" : 0,
    "C" : 0,
    "D" : 0,
    "E" : 0,
    "F" : 0,
    "G" : 0
}

n = int(input())

for i in range(n):
    line = input()
    letter_count = letter_count_proto.copy()
    
    for character in line:
        upper_case_character = character.upper()
        if upper_case_character in letter_count:
            letter_count[upper_case_character] += 1
            
    max_letter = None
    max_count = None
    for (letter, count) in letter_count.items():
        if max_count is None or count > max_count:
            max_letter = letter
            max_count = count
            
    print(max_letter)