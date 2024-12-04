# Import libraries
import numpy as np
from .utils import mutate


def schedule(iter, max_iter):
    return 1 - (iter + 1) / max_iter

def simulated_annealing(seq, model, max_iter):
    """ Simulated annealing for sequence sampling."""

    # Initialize the current state
    current_seq = seq
    current_state = model(current_seq)

    # Perform multiple iterations
    for iter in range(max_iter - 1):
        
        # Determine the schedule
        T = schedule(iter=iter, max_iter=max_iter)

        # Find a neighbour state
        neighbour_seq = mutate(current_seq)
        neighbour_state = model(neighbour_seq)

        # Preferred sequence will have a higher state (score)
        # A modification to the score is needed to avoid dividing the zero
        delta_E = neighbour_state - current_state + 0.01

        # Check for improvement
        if delta_E > 0:
            current_seq, current_state = neighbour_seq, neighbour_state
        else:
            if np.exp(delta_E/T) > np.random.random():
                current_seq, current_state = neighbour_seq, neighbour_state
    
    return current_seq
