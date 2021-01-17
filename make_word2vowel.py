import sys
import time
from Class import Vowel
from Class import Embeddings

def load_words(embeddings):
    words = []
    for word in embeddings.word2vec.vocab.keys():
        words.append(word)
    return words


def write_dictionary(words, vowel, fname):
    start = time.time()
    word_len = len(words)
    word_and_vowel = []
    print('word_len', word_len)
    for i, word in enumerate(words):
        word_vowel = vowel.word2vowel(word)
        # 文字列を逆に
        reversed_vowel = ''.join(list(reversed(word_vowel)))
        word_and_vowel.append([reversed_vowel, word])
        if i%10000 == 0:
            print(i, '/', word_len, 'time', time.time()-start)
    sorted_word_and_vowel = sorted(word_and_vowel, key = lambda x:x[0])

    for i in range(len(sorted_word_and_vowel)):
        sorted_word_and_vowel[i][0] = ''.join(list(reversed(sorted_word_and_vowel[i][0])))

    print(sorted_word_and_vowel)
    with open(fname, 'w') as fp:
        for word_and_vowel in sorted_word_and_vowel:
            fp.writelines(word_and_vowel[0]+'\t'+word_and_vowel[1])
            fp.writelines('\n')
    # 母音の5つの辞書に割り当てて、韻の母音でやれば5つの塊に分けれるな


def write_indexies(fname, indexies):
    with open(fname, 'w') as fp:
        for index in indexies:
            word_vowels = index[0]
            word = index[1]
            print(word_vowels)
            for word_vowel in word_vowels:
                fp.writelines(word_vowel+'\t'+word)
                fp.writelines('\n')

def main():

    embeddings = Embeddings.Embeddings(sys.argv[1])
    words = load_words(embeddings)
    vowel = Vowel.Vowel(sys.argv[2])
    write_dictionary(words, vowel, sys.argv[3])
    sys.exit()

    start = time.time()
    print('loading_word', start)
    words = load_words(sys.argv[2])
    print('loaded_word', time.time()-start)
    start = time.time()
    print('making_index', start)
    indexies = make_index(words, vowel)
    print('made_index', time.time()-start)
    write_indexies(sys.argv[3], indexies)
    print(indexies)


if __name__ == '__main__':
    main()
