import MeCab


class Mecab():

    def __init__(self):
        self.chasen_tokenizer = MeCab.Tagger('-Ochasen')
        self.input_words = []
        self.rhymes = []

    def tokenize(self, input_verse):
        nouns = [line for line in self.chasen_tokenizer.parse(input_verse).splitlines() if "名詞" in line.split()[-1]]
        self.input_words = []
        for noun in nouns:
            n = noun.split('\t')
            word = n[0]
            self.input_words.append(word)


def main():
    input_verse ='私は猫である。'
    tokenizer = Mecab()
    tokenizer.tokenize(input_verse)
    print(tokenizer.input_words)


if __name__ == '__main__':
    main()
