#-*-coding:utf-8-*-

from konlpy.tag import Mecab
from khaiii import KhaiiiApi
from kiwipiepy import Kiwi
import os
from typing import List

class Custom_Tokenizer:
    def __init__(self, tokenizer):
        assert tokenizer in {'khaiii', 'mecab', 'kiwi'}
        self.tokenizer = tokenizer
        if tokenizer == 'khaiii':
            self.tknizer = KhaiiiApi()
        elif tokenizer == 'mecab':
            self.tknizer = Mecab()
        elif tokenizer == 'kiwi':
            self.tknizer = Kiwi()
        print('Got {} tokenizer'.format(tokenizer))

    def use_khaiii(self, text):
        assert self.tokenizer == 'khaiii'
        result = list()
        for sent in self.tknizer.analyze(text):
            result += sent.morphs
        return [str(word) for word in result]

    def run_tokenizer(self, reviews: List[str], check=100000):

        def only_nouns(pair):
            'when use khaiii, get only NNG'
            if pair.split('/')[1]=='NNG': return True
        
        total = len(reviews)
        rst_morphs = list()
        rst_nouns = list()
        nums = 0

        if self.tokenizer == 'khaiii':
            for review in reviews:
                tknized = self.use_khaiii(review)
                rst_morphs.append(tknized)
                nouns = list(filter(only_nouns, tknized))
                rst_nouns.append(nouns)
                nums += 1
                if nums % check == 0:
                    print('  {:,}/{:,} processed'.format(nums, total))

        elif self.tokenizer == 'mecab':
            for review in reviews:
                morphs = self.tknizer.morphs(review)
                nouns = self.tknizer.nouns(review)
                rst_morphs.append(morphs)
                rst_nouns.append(nouns)
                nums += 1
                if nums % check == 0:
                    print('  {:,}/{:,} processed'.format(nums, total))

        elif self.tokenizer == 'kiwi':
            for review in reviews:
                tknized = self.tknizer.analyze(review)[0][:-1][0]
                rst_morphs.append([token.form for token in tknized])
                rst_nouns.append([token.form for token in tknized if token.tag == 'NNG'])
                nums += 1
                if nums % check == 0:
                    print('  {:,}/{:,} processed'.format(nums, total))
        
        return rst_morphs, rst_nouns

def export_tkd(data, dir, f_name):
    '''
    (sentence1)word1\tword2\tword3\n
    (sentence2)word1\tword2\tword3\n
    '''
    if dir and not os.path.exists(dir):
        os.mkdir(dir)
    with open(os.path.join(dir, f_name), 'w') as f:
        for review in data:
            f.write('\t'.join(review)+'\n')
    print('{} exported'.format(os.path.join(dir, f_name)))

def load_tkd(path) -> List[List[str]]:
    rst = list()
    with open(path, 'r') as f:
        for line in f:
            words = line.rstrip().split('\t')
            rst.append(words)
    print('{} loaded'.format(path))
    return rst