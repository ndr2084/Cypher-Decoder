from collections import Counter, defaultdict
import matplotlib.pyplot as plt
class CypherUtils:

    @staticmethod
    def frequency(cypher: list) -> dict:
        freq: dict = None
        if len(cypher) == 0:
            return freq
        for letter in cypher:
            freq = Counter(letter)
        return freq

    @staticmethod
    def keep_alpha(cypher: dict) -> dict:
        filtered_cypher = {k: v for k, v in cypher.items() if (k.isalpha())}
        return filtered_cypher

    @staticmethod
    def frequency_bigrams(cypher: list) -> dict:
        freq = defaultdict(int)
        for sentence in cypher:
            for x in range(len(sentence) - 1):
                if sentence[x].isalpha() and sentence[x+1].isalpha():
                    bigram = sentence[x:x+2]
                    freq[bigram] += 1
        return freq


    @staticmethod
    def transform_to_lower(cypher: list) -> list:
        lower_cypher = [word.lower() for word in cypher]
        return lower_cypher

    @staticmethod
    def transform_to_upper(cypher: list) -> list:
        upper_cypher = [word.upper() for word in cypher]
        return upper_cypher

    @staticmethod
    def display_frequency(cypher: dict) -> None:
        plt.bar(list(cypher.keys()), cypher.values(), color='g')
        plt.show()

    @staticmethod
    def sort_frequency(cypher: dict) -> dict:
        return dict(sorted(cypher.items(), reverse=True, key=lambda item: item[1]))

#    @staticmethod
#    def transform_swap_letters(cypher: list) -> list:










