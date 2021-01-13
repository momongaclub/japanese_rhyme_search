import sys


class Chat():

    def __init__(self):
        self.template = '{}よりも{}な{}つまり{}の{}だ'
        self.verse = ''

    def make_verse(self, rhymes):
        if rhymes[0] == 'None':
            self.verse = '辞書にありません'
        else:
            self.verse = self.template.format(rhymes[0], rhymes[1], rhymes[2], rhymes[3], rhymes[4])

if __name__ == '__main__':
    main()
