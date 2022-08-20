from manimlib import *

class TextExample(Scene): 
    def construct(self): 
        text = Text('Hello, world!').scale(3)
        self.add(text)

class TextColorExample(Scene): 
    def construct(self):
        text = Text(
            'Google', 
            t2c={
                (0,1):'#3174f0', (1,2):'#e53125', 
                (2,3):'#fbb003', (3,4):'#3174f0', 
                (4,5):'#269a43', (5,6):'#e53125',
            }
        ).scale(3)
        self.add(text)

script = '''
Hello
你好
こんにちは
안녕하세요
'''

class MultilingualTextExample(Scene):
    def construct(self):
        text = Text(script, font='Source Han Sans')
        self.add(text)