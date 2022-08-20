from manimlib import *
from manimgl_mathjax import *

class TestJTex(Scene):
    def construct(self):
        self.add(Tex(r"a&b&c\\d&e&f\\g&h&i"))


class TestText(Scene):
    def construct(self):
        # t1 = Text("123")
        axes = Axes(x_range=[-2,2,1], width=4)
        line = Line().add_tip(True).add_tip()
        # self.add(t1)
        self.add(axes)
        self.add(line)
        print(line.get_start(), line.get_end())

