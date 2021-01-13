import argparse
from gensim.models import KeyedVectors


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('embeddings', help='embeddings')
    args = parser.parse_args()
    return args


class Embeddings():

    def __init__(self, embeddings_fname):
        self.word2vec = self.load_embeddings(embeddings_fname)

    def load_embeddings(self, fname, f_type='pkl'):
        if f_type == 'pkl':
            return KeyedVectors.load(fname)
        elif f_type == 'bin':
            return KeyedVectors.load_word2vec_format(fname, binary=True)
        elif f_type == 'txt':
            return KeyedVectors.load_word2vec_format(fname)
        else:
            print('error')

    def save_pkl(self, fname):
        self.word2vec.save(fname+'pkl', pickle_protocol=1)


def main():
    args = parser()
    embeddings = Embeddings(args.embeddings)


if __name__ == '__main__':
    main()
