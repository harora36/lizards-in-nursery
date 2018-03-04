from lizards_in_nursery.state import State
import random


def simulated_annealing(arr, length, p):
    import timeit
    start_time = timeit.default_timer()
    curr_state = State(length, p)
    curr_state.assign_random_indexes(arr)
    cost = curr_state.calculate_cost(arr)
    iteration_count = 0
    while cost > 0 and iteration_count < 1000:
        temp = 100000
        elapsed = timeit.default_timer() - start_time
        if elapsed >= 298:
            return None
        while temp > 0 and cost != 0:
            elapsed = timeit.default_timer() - start_time
            print(str(elapsed))
            if elapsed >= 298:
                return None
            next_state = curr_state.transition(arr)
            next_state_cost = next_state.calculate_cost(arr)
            diff = cost - next_state_cost
            if diff > 0:
                curr_state = next_state
                cost = next_state_cost
            else:
                import math
                probability = math.exp(diff / temp)
                random_prob = random.random()
                if random_prob <= probability:
                    curr_state = next_state
                    cost = next_state_cost
            old_temp = temp
            temp = temp * 0.99
            if old_temp == temp:
                break
        iteration_count += 1
    return curr_state, cost
