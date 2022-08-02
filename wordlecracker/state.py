from english_words import english_words_set


class State:
    def __init__(self):
        self.not_in_word = []
        self.not_at_position = {0: [], 1: [], 2: [], 3: [], 4: []}
        self.at_position = {0: [], 1: [], 2: [], 3: [], 4: []}

    def addGray(self, word: str, index: int):
        letter = word[index]
        for i in range(0, 5):
            if letter in self.at_position:
                self.not_at_position[index].append(letter)
                return
        self.not_in_word.append(letter)
        # if len(word.replace(letter, '')) > len(word) - 2:
        #     self.not_in_word.append(letter)
        # else:
        #     self.not_at_position[index].append(letter)

    def addYellow(self, letter, index):
        self.not_at_position[index].append(letter)

    def addGreen(self, letter, index):
        self.at_position[index].append(letter)

    def addAttempt(self, word, results: tuple[int, int, int, int, int]):
        for i in range(0, len(word)):
            if results[i] == 1:
                self.addGray(word, i)
            if results[i] == 2:
                self.addYellow(word[i], i)
            if results[i] == 3:
                self.addGreen(word[i], i)

    def getRemainingWords(self):
        five_letter_words = [x for x in english_words_set if len(x) == 5]
        return [word for word in five_letter_words if
                self.satisfies_gray(word) and self.satisfies_yellow(word) and self.satisfies_green(word)]

    def satisfies_gray(self, word):
        for letter in self.not_in_word:
            if letter in word:
                return False
        return True

    def satisfies_yellow(self, word):
        for position in self.not_at_position:
            for letter in self.not_at_position[position]:
                if letter not in word or word[position] == letter:
                    return False
        return True

    def satisfies_green(self, word):
        for position in self.at_position:
            for letter in self.at_position[position]:
                if word[position] != letter:
                    return False
        return True
