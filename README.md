# PinMix

[![Build Status](https://travis-ci.org/lukaszkuczynski/pinmix.svg?branch=master)](https://travis-ci.org/lukaszkuczynski/pinmix)

Tool that mixes your Chinese text with Pinyin transcription, helping you to read your Chinese text.

## Usage

```bash
pinmix <filename>
```
For instance, having file `chinese.txt` with contents
```
我不会说中文很好
但pinmix可以帮助我
```
and running script with
```
pinmix chinese.txt
```
will result in following output
```
我不会说中文很好
wǒ bùhuì shuō zhōngwén hěn hǎo
但pinmix可以帮助我
dàn pinmix kěyǐ bāngzhù wǒ
```
