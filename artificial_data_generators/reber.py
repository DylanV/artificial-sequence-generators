import numpy as np

states = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

transitions = {0: [1, 2], 1: [3, 5], 2: [4, 7], 3: [3, 5], 4: [4, 7], 5: [6, 9],
               6: [4, 7], 7: [8, 10], 8: [9, 6], 9: [11], 10: [11]}

encodings = {0: 0, 1: 3, 2: 2, 3: 1, 4: 3, 5: 4, 6: 4, 7: 5, 8: 2, 9: 1, 10: 5, 11: 6}
decodings = {0: 'B', 1: 'S', 2: 'P', 3: 'T', 4: 'X', 5: 'V', 6: 'E'}
chars = {0: 'B', 1: 'T', 2: 'P', 3: 'S', 4: 'T', 5: 'X', 6: 'X', 7: 'V', 8: 'P', 9: 'S', 10: 'V', 11: 'E'}


def make_sequence():
    sequence = [states[0]]
    while sequence[-1] != states[-1]:
        sequence.append(np.random.choice(transitions[sequence[-1]]))

    sequence = [encodings[x] for x in sequence]

    return sequence


print([decodings[x] for x in make_sequence()])

