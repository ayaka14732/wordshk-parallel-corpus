import os
from random import Random
import seed

with open('plus15/yue.txt', encoding='utf-8') as f:
    sentences_yue = [line.rstrip('\n') for line in f]

with open('plus15/en.txt', encoding='utf-8') as f:
    sentences_en = [line.rstrip('\n') for line in f]

sentences = list(zip(sentences_yue, sentences_en))

rng = Random(seed.BUDDHA)
rng.shuffle(sentences)

n_sentences = len(sentences)

dev_len = 1500
test_len = 1500
train_len = n_sentences - dev_len - test_len

train = sentences[:train_len]
dev = sentences[train_len:train_len + dev_len]
test = sentences[-test_len:]

with open('plus15/train.yue.txt', 'w', encoding='utf-8') as f1, \
        open('plus15/train.en.txt', 'w', encoding='utf-8') as f2:
    for yue, en in train:
        print(yue, file=f1)
        print(en, file=f2)

with open('plus15/dev.yue.txt', 'w', encoding='utf-8') as f1, \
        open('plus15/dev.en.txt', 'w', encoding='utf-8') as f2:
    for yue, en in dev:
        print(yue, file=f1)
        print(en, file=f2)

with open('plus15/test.yue.txt', 'w', encoding='utf-8') as f1, \
        open('plus15/test.en.txt', 'w', encoding='utf-8') as f2:
    for yue, en in test:
        print(yue, file=f1)
        print(en, file=f2)

os.remove('plus15/yue.txt')
os.remove('plus15/en.txt')
