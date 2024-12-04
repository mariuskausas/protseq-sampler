# Import libraries
import numpy as np
from .utils import mutate


def hill_climb(seq, model, iter):
    """ Hill Climb for sequence sampling."""
    current_seq = seq
    current_state = model(current_seq)
    for i in range(iter):
        neighbour_seq = mutate(current_seq)
        neighbour_state = model(neighbour_seq)
        if neighbour_state > current_state:
            current_seq, current_state = neighbour_seq, neighbour_state
    return current_seq
