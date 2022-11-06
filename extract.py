import csv
from glob import glob
import regex as re

def replace_hash(s: str) -> str:
    '''
    >>> replace_hash('因為個#計劃 有需要改動嘅地方，所以唯有延緩#執行。')
    '因為個計劃有需要改動嘅地方，所以唯有延緩執行。'
    >>> replace_hash('#Mac OS')
    'Mac OS'
    '''
    s = re.sub(r'#([\p{Unified_Ideograph}\u3006\u3007]+) (?=[\p{Unified_Ideograph}\u3006\u3007。，？！《》（）])', r'\1', s)  # 成嚿中文+空格+中文或中文標點
    s = s.replace('#', '')
    return s

def remove_space(s: str) -> str:
    '''
    >>> remove_space('摸 A B 12至 3')
    '摸A B 12至3'
    >>> remove_space('噉你哋要唔要呢 ？')
    '噉你哋要唔要呢？'
    '''
    s = re.sub(r'(?<=[\p{Unified_Ideograph}\u3006\u3007]) (?=[\da-zA-Z！，：？《》])', r'', s)
    s = re.sub(r'(?<=[\da-zA-Z！，：？《》]) (?=[\p{Unified_Ideograph}\u3006\u3007])', r'', s)
    return s

all_texts = []
filename = glob('all-*.csv')[-1]
with open(filename, newline='') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        if len(row) < 3:
            continue
        row = row[2]
        if '<eg>' in row:
            all_texts.append(row)

def is_paren_balanced(yue: str, en: str) -> bool:
    a = yue.count('（')
    b = yue.count('）')
    c = en.count('(')
    d = en.count(')')
    return a == b == c == d

def should_keep(yue: str, en: str) -> bool:
    if en in ('X', 'x'):
        return False
    if re.search(r'[\p{Unified_Ideograph}\u3006\u3007]', en):  # 有漢字
        return False
    if not is_paren_balanced(yue, en):
        return False
    if en.startswith('literally:') or en.startswith('Literally:'):
        return False
    return True

def g(s: str):
    return len(s[0]), s[0], s[1], s[2]

def f():
    seen = set()
    for text in all_texts:
        for match in re.finditer(r'<eg>\nyue:(.+?) ?\(([^(\n]+)\)\neng:(.+)', text):
            yue, jyp, en = match.groups((1, 2, 3))

            if (m := re.fullmatch(r'(.+?)[;,] literally.+', en)):
                en = m[1]
            if (m := re.fullmatch(r'(.+?\.) Literally:.+', en)):
                en = m[1]
            if (m := re.fullmatch(r'(.+?); literal meaning.+', en)):
                en = m[1]

            if (m := re.fullmatch(r'(.+?)[;,] figuratively.+', en)):
                en = m[1]

            if (m := re.fullmatch(r'(.+?)[;,]? i\.e\..+', en)):
                en = m[1]

            if ';' in en:
                if len(yue) <= 6 or en[-1] not in '.!?':
                    en = en.split(';', 1)[0]  # take the first explanation

            if not should_keep(yue, en) or yue in seen:
                continue
            yield yue, jyp, en
            seen.add(yue)
all_sentences = list(sorted(f(), key=g))

with open('all/yue.txt', 'w', encoding='utf-8') as f1, \
        open('all/yue-Latn.txt', 'w', encoding='utf-8') as f2, \
        open('all/en.txt', 'w', encoding='utf-8') as f3:
    for a, b, c in all_sentences:
        a = remove_space(replace_hash(a))
        if len(a) > 2:
            print(a, file=f1)
            print(b, file=f2)
            print(c, file=f3)
