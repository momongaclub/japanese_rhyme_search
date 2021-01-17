import sys
import pykakasi


class Vowel():

    def __init__(self, vowel_dict):
        self.vowel = ''
        self.yomi = ''
        self.vowel2word = self.load_vowel2word(vowel_dict)

    def load_vowel2word(self, fname):
        vowel2word = {}
        with open(fname, 'r') as fp:
            for line in fp:
                line = line.rstrip('\n')
                line = line.split('\t')
                vowel = line[0]
                word = line[1]
                if vowel2word.get(vowel) == None:
                    vowel2word[vowel] = [word]
                else:
                    vowel2word[vowel].append(word)
        return vowel2word

    def word2yomi(self, word):
        # TODO  正式に決まり次第音韻表記へ変更する
        # TODO 数値、記号が変換出来ていない
        kakasi = pykakasi.kakasi()
        kakasi.setMode("H","a") # Hiragana to ascii, default: no conversion
        kakasi.setMode("K","a") # Katakana to ascii, default: no conversion
        kakasi.setMode("J","a") # Japanese to ascii, default: no conversion
        kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table
        # kakasi.setMode("s", True) # add space, default: no separator
        # kakasi.setMode("C", True) # capitalize, default: no capitalize
        converter = kakasi.getConverter()
        yomi = converter.do(word)
        return yomi

    def word2vowel(self, word):
        yomi = self.word2yomi(word)
        vowel = ''
        # TODO 正規表現 使いましょう
        v_list = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O', 'n']
        for w in yomi:
            if w in v_list:
                vowel = vowel + w
        return vowel

    def yomi2cons(self, yomi):
        cons = ''
        v_list = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O', 'n']
        for w in yomi:
            if w not in v_list:
                cons = cons + w 
        return cons


def main():
    word = 'プール学校'
    vowel = Vowel()
    yomi = vowel.word2yomi(word)
    print(yomi)

if __name__ == '__main__':
    main()
