from Class import Corpus
from Class import Vowel
from Class import Tokenizer
from Class import Search

import argparse
import gensim
import time
import sys


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('query_word', help='query word')
    args = parser.parse_args()
    return args


def main():
    args = parse()
    query_word = args.query_word

    word_embeddings = Corpus.Corpus()
    vowel = Vowel.Vowel()
    search = Search.Search()
    print('load_embeddings')
    word_embeddings.load_corpus('./hottolink.pkl', f_type='pkl')
    rhymes = search.search_rhyme(tokenizer.input_words, word_embeddings, vowel)

    print(rhymes)
    print(search.results)
    return rhymes


if __name__ == '__main__':
    main()
