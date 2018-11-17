# PinMix

[![Build Status](https://travis-ci.org/lukaszkuczynski/pinmix.svg?branch=master)](https://travis-ci.org/lukaszkuczynski/pinmix)

Tool that mixes your Chinese text with Pinyin transcription, helping you to read your Chinese text.

## Installation
Tool to be use straight from the pypi index.
```bash
pip install pinmix
```

## Basic usage

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

## Output options
If the 2nd argument is not passed to pinmix tool it will just print the result to the standard output.  Otherwise it will create ODT file that can be read f.e. by OpenOffice.  That file will contain output of the transformation parts put in different styles. It makes possible to you to make your pinyin or the original parts different by applying different formatting to them.
The example of that kind of usage is the following:
```bash
pinmix chinese.txt chinesedoc.odt
```
It will create open office doc based on pinmix transformation.