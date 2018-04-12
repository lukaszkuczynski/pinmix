import jieba
from xpinyin import Pinyin


sentence = "我想说更好的中文，但很难，因为我是波兰人"
print(sentence)

segments = jieba.cut(sentence)
output = " ".join(segments)
print(output)

p = Pinyin()
pinyined = p.get_pinyin(output, splitter='', show_tone_marks=True)
print(pinyined)
