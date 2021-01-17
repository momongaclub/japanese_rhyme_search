from Class import Embeddings
from Class import Vowel
from Class import Search

import argparse


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('query_word', help='query word')
    parser.add_argument('embeddings', help='embeddings')
    parser.add_argument('vowel_dict', help='vowel_dict')
    args = parser.parse_args()
    return args


def main():
    args = parse()
    query_word = args.query_word
    embeddings = Embeddings.Embeddings(args.embeddings)
    vowel = Vowel.Vowel(args.vowel_dict)
    search = Search.Search(match_n=5)
    rhymes = search.search_rhyme(query_word, embeddings, vowel)
    print(rhymes)
    return rhymes


if __name__ == '__main__':
    main()
