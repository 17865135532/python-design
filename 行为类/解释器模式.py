#!/usr/bin/python
# -*- encoding: utf-8 -*-

# 要开发一个自动识别谱子的吉他模拟器，达到录入谱即可按照谱发声的效果。
# 除了发声设备外（假设已完成），最重要的就是读谱和译谱能力了。
# 分析其需求，整个过程大致上分可以分为两部分：
# 根据规则翻译谱的内容；根据翻译的内容演奏。
# 我们用一个解释器模型来完成这个功能。

"""
意图： 给定一个语言， 定义它的文法表示，并定义一个解释器
主要解决： 对于一些固定文法构建一个解释句子的解释器

实例：
俩部分 1、转义谱   2、演奏谱
"""


class PlayContent():
    play_text = None


class Expression():

    def interpret(self, context):
        if len(context.play_text) == 0:
            return
        else:
            play_segs = context.play_text.split(" ")
            for play_seg in play_segs:
                pos = 0  # 检测字母 长度
                for ele in play_seg:
                    if ele.isalpha():
                        pos += 1
                        continue
                    break
                play_chord = play_seg[0:pos]
                play_valeu = play_seg[pos:]
                self.excute(key=play_chord, value=play_valeu)

    def excute(self, key, value):
        ...


class NormGuitar(Expression):
    def excute(self, key, value):
        print(f"key: {key}, value: {value}")


def main():
    context = PlayContent()
    context.play_text = "C53231323 Em43231323 F43231323 G63231323"
    guitar = NormGuitar()
    guitar.interpret(context)


if __name__ == '__main__':
    main()
