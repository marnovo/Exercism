#
# Exercism.io
# Python track
# Problem Extra #2 - Pangram
# github.com/marnovo/Exercism
#


def is_pangram(sentence):
    # set of letters and 0s
    all_letters = [[chr(l), 0] for l in range(ord('a'), ord('z'))]
    # for each letter, check if present in the sentence, if so, set 0 to 1
    for letter in all_letters:
        for char in sentence.lower():
            if char == letter[0]:
                letter[1] = 1
    # if all letters set to 1, it's a pangram
    if sum(row[1] for row in all_letters) == len(all_letters):
        return True
    else:
        return False
