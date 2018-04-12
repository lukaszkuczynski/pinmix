import jieba
from xpinyin import Pinyin


def line_to_pinyin(line):
    segments = jieba.cut(line)
    output = " ".join(segments)
    print(output)
    p = Pinyin()
    pinyined = p.get_pinyin(output, splitter='', show_tone_marks=True)
    return pinyined
