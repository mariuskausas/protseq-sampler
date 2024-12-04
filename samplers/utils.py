# Import libraries
import numpy as np

# Define AA single letter library
AA_single_letter = [ 'A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

def choose_random_position(seq):
    """ Choose a random position in an amino acid sequence."""
    pos = np.random.randint(0, len(seq))
    return pos


def mutate(seq):
    """ Mutate a given amino acid sequence."""
    pos = choose_random_position(seq)
    mut = np.random.choice(AA_single_letter)
    if pos >= len(seq):
        return seq
    else:
        new_seq = seq[:pos] + mut + seq[pos + 1:]
    return new_seq


def dummy_alanine_preference(seq):
    """ Dummy model to for alanine preference design."""
    return seq.count("A")
