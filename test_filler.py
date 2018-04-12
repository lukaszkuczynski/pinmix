from unittest import TestCase
from filler import line_to_pinyin


class FillerTest(TestCase):
    
    def test_line_is_converted(self):
        chinese_text = "波兰人"
        pinyined = line_to_pinyin(chinese_text)
        self.assertEquals(pinyined, "bōlánrén")

