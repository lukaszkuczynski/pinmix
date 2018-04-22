import jieba
from xpinyin import Pinyin
import re
import logging

def line_to_pinyin(line):
    jieba.setLogLevel(logging.ERROR)
    segments = jieba.cut(line)
    output = " ".join(segments)
    p = Pinyin()
    pinyined = p.get_pinyin(output, splitter='', show_tone_marks=True)
    return pinyined

def is_chinese(line):
    matches = re.findall(r'[\u4e00-\u9fff]+', line)
    return len(matches) > 0

def process_file(filename):
    with open(filename, encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if is_chinese(line):
                print(line)
                print(line_to_pinyin(line))
            else:
                print(line)

