from state import State
from word_ranker import get_best_next_word

if __name__ == '__main__':
    state = State()
    # state.addAttempt("fried", (1,1,1,1,1))
    # state.addAttempt("salon", (1,1,2,2,1))
    # state.addAttempt("cloth", (3,2,2,1,1))

    remaining = state.getRemainingWords()
    print(remaining)
    print(len(remaining))

    print(get_best_next_word(state))
