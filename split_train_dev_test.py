with open('all/yue.txt', encoding='utf-8') as f:
    sentences_yue = [line.rstrip('\n') for line in f]

with open('all/en.txt', encoding='utf-8') as f:
    sentences_en = [line.rstrip('\n') for line in f]

sentences = list(zip(sentences_yue, sentences_en))

plus15 = []
minus15 = []

with open('plus15/yue.txt', 'w', encoding='utf-8') as f1, \
        open('plus15/en.txt', 'w', encoding='utf-8') as f2, \
        open('minus15/yue.txt', 'w', encoding='utf-8') as f3, \
        open('minus15/en.txt', 'w', encoding='utf-8') as f4:
    for yue, en in sentences:
        if len(yue) >= 15:
            print(yue, file=f1)
            print(en, file=f2)
        else:
            print(yue, file=f3)
            print(en, file=f4)
