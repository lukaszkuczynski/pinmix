from unittest import TestCase
from pinmix.filler import line_to_pinyin, is_chinese


class FillerTest(TestCase):
    
    def test_line_is_converted(self):
        chinese_text = "波兰人"
        pinyined = line_to_pinyin(chinese_text)
        self.assertEqual(pinyined, "bōlánrén")

    def test_can_discern_if_line_is_chinese(self):
        chinese_line = "波兰人"
        not_chinese_line = "This is not Chinese!"
        self.assertFalse(is_chinese(not_chinese_line))
        self.assertTrue(is_chinese(chinese_line))

