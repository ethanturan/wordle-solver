from copy import deepcopy
from state import State
from itertools import product


def get_minimum_eliminations(state: State, test_word: str, current_count: int):
    potential_states = list(product(range(1, 4), repeat=5))
    potential_eliminations = []
    for test_state in potential_states:
        copy = deepcopy(state)
        copy.addAttempt(test_word, test_state)
        # total words minus remaining words equals number eliminated
        potential_eliminations.append(current_count - len(copy.getRemainingWords()))
    print("potential eliminations for: ", test_word)
    print("min value: ", min(potential_eliminations))
    print(potential_eliminations)
    # Grab the minimum number eliminated. This will be the safest
    return min(potential_eliminations)


def get_best_next_word(state: State):
    remaining_words = state.getRemainingWords()
    potential_words: dict[str, int] = {}
    current_count = len(state.getRemainingWords())
    for word in remaining_words:
        potential_words[word] = get_minimum_eliminations(state, word, current_count)
        # Grab the word with the highest minimum number of eliminations. This will give the best safest move.
    return max(potential_words, key=potential_words.get)
