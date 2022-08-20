from manimlib import *


class ChangingDecimalExample(Scene):
    def construct(self):
        number = DecimalNumber(0, text_config={"font": "monospace"}).scale(2)

        def update_func(t):
            return t * 10
        self.add(number)
        self.wait()
        self.play(ChangingDecimal(number, update_func), run_time=3)
        self.wait()


class ChangeDecimalToValueExample(Scene):
    def construct(self):
        number = DecimalNumber(0, text_config={"font": "monospace"}).scale(2)
        self.add(number)
        self.wait()
        self.play(ChangeDecimalToValue(number, 20), run_time=3)
        self.wait()


class CountInFromExample(Scene):
    def construct(self):
        number = DecimalNumber(10, text_config={"font": "monospace"}).scale(2)
        self.add(number)
        self.play(CountInFrom(number, 0))
        self.wait()