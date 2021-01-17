import time

class Search():

    def __init__(self, match_n):
        self.results = []
        self.match_n = match_n

    def search_rhyme(self, query_word, corpus, vowel):
        rhymes = ''
        start_time = time.time()
        query_vowel = vowel.word2vowel(query_word)
        query_yomi = vowel.word2yomi(query_word)
        print('query_info: word「{0}」 vowel「{1}」 yomi「{2}」'.format(query_word, query_vowel, query_yomi))
        results = []
        match_weight = 0.9
        cosine_weight = 1 - match_weight
        # for i, word in enumerate(corpus.word2vec.vocab):
        for target_vowel, word in vowel.vowel2word.items():
            # print('target_vowel', target_vowel,'word', word)
            # ここで変換すると遅い
            # word_vowel = vowel.word2vowel(word)
            # word_yomi = vowel.word2yomi(word)
            # 末尾からn文字母音が一致すれば
            if target_vowel.endswith(query_vowel[-self.match_n:]):
                # word_match_score, scores = self.word_match_scorer(vowel, query_yomi, word_yomi)
                # cosine_score = self.cosine_similarity(corpus, query_word, word)
                # score = match_weight*word_match_score + cosine_weight*cosine_score
                score = 1
                result = [word, target_vowel, score]
                results.append(result)
                # rhymes = rhymes + word + '(' + word_vowel + ')' + ','
        # score順にソート
        results = sorted(results, key=lambda x:x[2], reverse=True)

        rhymes = []
        for result in results:
            words = result[0]
            word_vowel = result[1]
            for word in words:
                # rhyme = word+'('+word_vowel+')'
                if word[0] == '[' and word[-1] == ']':
                    rhyme = word[1:-1]
                else:
                    rhyme = word
                rhymes.append(rhyme)
            # self.results.append(word)
        return rhymes


    def word_match_scorer(self, vowel, query_yomi, word_yomi, vowel_weight=0.2, cons_weight=0.2, word_len_weight=0.1):
        # TODO とりあえず編集距離
        word_vowel = vowel.word2vowel(word_yomi)
        query_vowel = vowel.word2vowel(query_yomi)
        word_cons = vowel.yomi2cons(word_yomi)
        query_cons = vowel.yomi2cons(query_yomi)
        vowel_score = 1 #Levenshtein.distance(word_vowel, query_vowel)
        cons_score = 1 #Levenshtein.distance(word_cons, query_cons)
        word_len = len(word_yomi)
        word_match_score = word_len_weight*word_len - (vowel_weight*vowel_score + cons_weight*cons_score)
        scores = [vowel_score, cons_score, word_len, word_match_score]
        return word_match_score, scores

    def cosine_similarity(self, corpus, query_word, target_word):
        cos_sim = corpus.word2vec.similarity(query_word, target_word)
        return cos_sim
