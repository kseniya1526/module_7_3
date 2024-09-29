import io
from pprint import pprint
class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = list(file_names)


    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':']
                    for punct in punctuation:
                        line = line.replace(punct, '')
                    line = line.replace(' - ', ' ')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        finded = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                finded[key] = value.index(word.lower()) + 1
        return finded

    def count(self, word):
        counted = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counted[value] = words_count
        return counted


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

