class Search():

    def __init__(self):
        self.results = []
        self.match_n = 2

    def search_rhyme(self, input_words, corpus, vowel):
        rhymes = ''
        for input_word in input_words:
            print(input_word)

        query_word = input_words[0]
        query_vowel = vowel.word2vowel(query_word)
        query_yomi = vowel.word2yomi(query_word)

        results = []
        cnt = 0
        match_n = 2
        match_weight = 0.3
        cosine_weight = 1 - match_weight

        print('target_word', query_word, 'vowel', query_vowel)
        for word in corpus.word2vec.vocab:
            word_vowel = vowel.word2vowel(word)
            word_yomi = vowel.word2yomi(word)
            if query_vowel[-match_n:] == word_vowel[-match_n:]:
                word_match_score, scores = self.word_match_scorer(vowel, query_yomi, word_yomi)
                cosine_score = self.cosine_similarity(corpus, query_word, word)

                score = match_weight*word_match_score + cosine_weight*cosine_score
                result = [word, word_vowel, score]
                results.append(result)
                rhymes = rhymes + word + '(' + word_vowel + ')' + ','
            cnt += 1
            if cnt == 2000:
                break
        results = sorted(results, key=lambda x:x[2], reverse=True) # scoreでソート

        rhymes = []
        for result in results:
            word = result[0]
            word_vowel = result[1]
            rhyme = word+'('+word_vowel+')'
            rhymes.append(rhyme)
            self.results.append(word)
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
