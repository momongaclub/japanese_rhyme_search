import time
import Levenshtein

class Search():

    def __init__(self, match_n, same_vowel_len=False):
        self.results = []
        self.match_n = match_n
        self.same_vowel_len = same_vowel_len

    def search_rhyme(self, query_word, corpus, vowel):
        rhymes = ''
        query_vowel = vowel.word2vowel(query_word)
        query_yomi = vowel.word2yomi(query_word)
        print('query_info: word「{0}」 vowel「{1}」 yomi「{2}」'.format(query_word, query_vowel, query_yomi))
        results = []
        match_weight = 0.05
        cosine_weight = 1 - match_weight
        # for i, word in enumerate(corpus.word2vec.vocab):
        for target_vowel, target_words in vowel.vowel2word.items():
            # print('target_vowel', target_vowel,'word', word)
            # ここで変換すると遅い
            # word_vowel = vowel.word2vowel(word)
            # word_yomi = vowel.word2yomi(word)
            # 末尾からn文字母音が一致すれば
            if target_vowel.endswith(query_vowel[-self.match_n:]):
                word_match_score = self.word_match_scorer(query_vowel, target_vowel)
                for target_word in target_words:
                    try:
                        cosine_score = self.cosine_similarity(corpus, query_word, target_word)
                    except:
                        cosine_score = 0
                    score = match_weight*word_match_score + cosine_weight*cosine_score
                    result = [target_word, target_vowel, score]
                    results.append(result)

        # score順にソート
        results = sorted(results, key=lambda x:x[2], reverse=True)
        # print('results', results)

        rhymes = []
        for result in results:
            target_word = result[0]
            if target_word[0] == '[' and target_word[-1] == ']':
                rhyme = target_word[1:-1]
            else:
                rhyme = target_word
            rhymes.append(rhyme)
        return rhymes


    def word_match_scorer(self, query_vowel, target_vowel):
        # vowel_score = Levenshtein.distance(query_vowel, target_vowel)
        # 逆順から回す[::-1]
        vowel_score = 0
        for qv, tv in zip(query_vowel[::-1], target_vowel[::-1]):
            if qv == tv:
                vowel_score += 1
        return vowel_score

    def cosine_similarity(self, embeddings, query_word, target_word):
        cos_sim = embeddings.word2vec.similarity(query_word, target_word)
        return cos_sim
